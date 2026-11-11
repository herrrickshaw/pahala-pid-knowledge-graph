"""Score pid-to-kg extractions against PID2Graph OPEN100 ground truth.
Usage: python score.py <extract_dir> <gt_dir> [pages...]   (page N <-> GT file N-1)"""
import json,sys,math,glob,itertools,collections,os
import networkx as nx
from PIL import Image
SEM=('valve','instrumentation','inlet/outlet','tank','pump','general')
PRIM=('connector','crossing','arrow')
def ctr(d): return ((float(d['xmin'])+float(d['xmax']))/2,(float(d['ymin'])+float(d['ymax']))/2)

# ---------- ground truth: semantic nodes + collapsed edges
def load_gt(path,drop=frozenset()):
    g=nx.read_graphml(path)
    for n in drop: g.nodes[n]['label']='connector'   # unrecorded fittings act as pass-through
    sem={n:d for n,d in g.nodes(data=True) if d['label'] in SEM}
    # 'crossing' nodes in PID2Graph are corners/tee junctions (degree 1-3), so they are ordinary line primitives
    h=nx.Graph()
    for n,d in g.nodes(data=True):
        if d['label'] in SEM+PRIM: h.add_node(n,**d)
    for u,v in g.edges():
        if g.nodes[u]['label']=='background' or g.nodes[v]['label']=='background': continue
        h.add_edge(u,v)
    # components of primitive-only subgraph
    prim=h.subgraph([n for n,d in h.nodes(data=True) if d['label'] in PRIM])
    edges=set()
    for comp in nx.connected_components(prim):
        att=set()
        for p in comp:
            for m in h.neighbors(p):
                if h.nodes[m]['label'] in SEM: att.add(m)
        for a,b in itertools.combinations(sorted(att),2): edges.add((a,b))
    for u,v in h.edges():  # direct semantic-semantic
        if u in sem and v in sem: edges.add(tuple(sorted((u,v))))
    return sem,edges

# ---------- our extraction: items + collapsed edges
VALVE_WORDS=('valve','prv','psv','relief')
def our_class(group,e):
    k=(e.get('kind') or '').lower()
    if group=='instruments': return 'instrumentation'
    if group=='off_page_connectors': return 'inlet/outlet'
    if group=='boundaries': return 'boundary'
    if group=='components':
        return 'valve' if any(w in k for w in VALVE_WORDS) else 'general'
    if group=='equipment':
        if any(w in k for w in('tank','vessel','sump','basin','drum','clarifier')): return 'tank'
        if 'pump' in k: return 'pump'
        return 'general'
def load_ours(path,return_adj=False):
    d=json.load(open(path)); items={}
    for grp in('equipment','components','instruments','off_page_connectors','boundaries'):
        for e in d.get(grp,[]):
            b=e.get('bbox')
            items[e['id']]={'cls':our_class(grp,e),'bbox':b,'grp':grp,'tag':e.get('tag')}
    # segments: component sets
    lines={l['id']:l for l in d.get('lines',[])}
    comps=collections.defaultdict(set)
    def seq(l): return [l['from']]+list(l.get('path',[]))+[l['to']]
    def node_of(x):  # endpoint -> list of ('seg',line,idx) or item id
        return x
    segid=lambda lid,i:('seg',lid,i)
    for lid,l in lines.items():
        s=seq(l)
        for i in range(len(s)-1):
            for x in (s[i],s[i+1]):
                if isinstance(x,str) and x in items: comps[segid(lid,i)].add(x)
    def seg_at(ref):  # tee point -> segment key
        lid=ref['line']; l=lines.get(lid)
        if not l: return None
        s=seq(l); after=ref.get('after')
        if after and after in s: i=s.index(after)
        else: i=0
        i=min(i,len(s)-2)
        return segid(lid,i)
    for lid,l in lines.items():
        s=seq(l)
        for k in('from','to'):
            x=l[k]
            if isinstance(x,dict):
                key=seg_at(x)
                if key:
                    other=l['to'] if k=='from' else l['from']
                    # the branch's own segment (first or last) joins the tee component
                    own=segid(lid,0 if k=='from' else len(s)-2)
                    comps[key]|=comps[own]
                    comps[own]=comps[key]
    for ins in d.get('instruments',[]):
        m=ins.get('measures')
        if not m: continue
        if m.get('item') in items and items[m['item']]['grp']!='components':
            comps[('m',ins['id'])]|={ins['id'],m['item']}
        elif m.get('line'):
            key=seg_at(m); 
            if key: comps[key].add(ins['id'])
    for s in d.get('signals',[]):
        a,b=s['from'],s['to']
        if a in items and b in items: comps[('s',a,b)]|={a,b}
    edges=set()
    for c in comps.values():
        for a,b in itertools.combinations(sorted(c),2): edges.add((a,b))
    adj=set()
    def add(a,b):
        if isinstance(a,str) and isinstance(b,str) and a in items and b in items and a!=b: adj.add(tuple(sorted((a,b))))
    for lid,l in lines.items():
        sq=seq(l)
        for i in range(len(sq)-1): add(sq[i],sq[i+1])
        for k in('from','to'):
            x=l[k]
            if isinstance(x,dict) and x.get('line') in lines:
                ml=seq(lines[x['line']]); after=x.get('after'); i=ml.index(after) if after in ml else 0
                nxt=ml[i+1] if i+1<len(ml) else None
                br=sq[1] if k=='from' else sq[-2]
                add(br,ml[i] if (after in ml) else None); add(br,nxt)
    if return_adj: return items,edges,adj
    return items,edges

COARSE={'tank':'equipment','pump':'equipment','general':'equipment'}
def match(gt_sem,ours,W,H,r,same_class=True,coarse=False):
    cm=(lambda c:COARSE.get(c,c)) if coarse else (lambda c:c)
    cand=[]
    for oid,o in ours.items():
        if not o['bbox']: continue
        ox=(o['bbox'][0]+o['bbox'][2])/2*W; oy=(o['bbox'][1]+o['bbox'][3])/2*H
        for gid,gd in gt_sem.items():
            if same_class and cm(gd['label'])!=cm(o['cls']): continue
            gx,gy=ctr(gd); dist=math.hypot(ox-gx,oy-gy)
            if dist<=r*W: cand.append((dist,oid,gid))
    cand.sort(); used_o=set(); used_g=set(); m={}
    for dist,oid,gid in cand:
        if oid in used_o or gid in used_g: continue
        used_o.add(oid); used_g.add(gid); m[oid]=gid
    return m

def prf(tp,fp,fn):
    p=tp/(tp+fp) if tp+fp else 0.0; r=tp/(tp+fn) if tp+fn else 0.0
    return p,r,(2*p*r/(p+r) if p+r else 0.0)

def main():
    ex,gtd=sys.argv[1],sys.argv[2]; pages=[int(x) for x in sys.argv[3:]] or list(range(1,13))
    rad=[0.01,0.02,0.04]; tot={r:collections.defaultdict(lambda:[0,0,0]) for r in rad}
    etot={r:[0,0,0,0,0] for r in rad}  # tp, fp(matched-only), fn(matched-only), gt_all, ours_all
    ptot={r:[0,0,0,0,0] for r in rad}  # process-only edges (no instrumentation endpoints)
    rows=[]
    for pg in pages:
        gp=os.path.join(gtd,f'{pg-1}.graphml'); ep=os.path.join(ex,f'page_{pg:02d}.json')
        if not os.path.exists(ep): continue
        W,H=Image.open(os.path.join(gtd,f'{pg-1}.png')).size
        gsem,gedges=load_gt(gp); items,oedges=load_ours(ep)
        for r in rad:
            m=match(gsem,items,W,H,r)
            for cls in SEM:
                gn=[n for n,d in gsem.items() if d['label']==cls]; on=[o for o,i in items.items() if i['cls']==cls]
                tp=sum(1 for o in on if o in m); tot[r][cls][0]+=tp; tot[r][cls][1]+=len(on)-tp; tot[r][cls][2]+=len(gn)-tp
            inv={g:o for o,g in m.items()}
            og={frozenset((m[a],m[b])) for a,b in oedges if a in m and b in m}
            gg={frozenset(e) for e in gedges}
            gg_m={e for e in gg if all(x in inv for x in e)}
            tp=len(og&gg); fp=len(og-gg); fn=len(gg_m-og)
            e=etot[r]; e[0]+=tp;e[1]+=fp;e[2]+=fn;e[3]+=len(gg);e[4]+=len(og)
            noi=lambda e_,cls: all(cls(x)!='instrumentation' for x in e_)
            ggp={e_ for e_ in gg if noi(e_,lambda x:gsem[x]['label'])}
            ogp={e_ for e_ in og if noi(e_,lambda x:gsem[x]['label'])}
            ggp_m={e_ for e_ in ggp if all(x in inv for x in e_)}
            tp=len(ogp&ggp); fp=len(ogp-ggp); fn=len(ggp_m-ogp)
            q=ptot[r]; q[0]+=tp;q[1]+=fp;q[2]+=fn;q[3]+=len(ggp);q[4]+=len(ogp)
        rows.append(pg)
    print('pages scored:',rows)
    # ---- coarse pass: equipment-like classes merged; edges clique vs adjacency
    ctot={r:[0,0,0] for r in rad}; E={r:{'clique':[0,0,0,0],'adj':[0,0,0,0]} for r in rad}
    for pg in rows:
        W,H=Image.open(os.path.join(gtd,f'{pg-1}.png')).size
        gsem,gedges=load_gt(os.path.join(gtd,f'{pg-1}.graphml')); items,oed,adj=load_ours(os.path.join(ex,f'page_{pg:02d}.json'),True)
        for r in rad:
            m=match(gsem,items,W,H,r,coarse=True); inv={g:o for o,g in m.items()}
            drop={n for n,d in gsem.items() if d['label']=='general' and n not in inv}
            gsem2,gedges2=load_gt(os.path.join(gtd,f'{pg-1}.graphml'),drop); gg={frozenset(e) for e in gedges2}
            ge_=[n for n,d in gsem.items() if d['label'] in('tank','pump','general')]; oe_=[o for o,i in items.items() if i['cls'] in('tank','pump','general')]
            tp=sum(1 for o in oe_ if o in m); ctot[r][0]+=tp;ctot[r][1]+=len(oe_)-tp;ctot[r][2]+=len(ge_)-tp
            for name,eds in(('clique',oed),('adj',adj)):
                og={frozenset((m[a],m[b])) for a,b in eds if a in m and b in m}
                gm={e for e in gg if all(x in inv for x in e)}; og={e for e in og if e in gg or all(x in gsem2 for x in e)}
                q=E[r][name]; q[0]+=len(og&gg);q[1]+=len(og-gg);q[2]+=len(gm-og);q[3]+=len(gg)
    print('\n##### COARSE (equipment-like classes merged) #####')
    for r in rad:
        tp,fp,fn=ctot[r]; p,rc,f=prf(tp,fp,fn)
        print(f'r={r*100:.0f}% equipment+other symbols: GT {tp+fn} ours {tp+fp} P {p:.2f} R {rc:.2f} F1 {f:.2f}')
        for name in('clique','adj'):
            tp,fp,fn,ga=E[r][name]; p,rc,f=prf(tp,fp,fn); print(f'   edges[{name:6s}] among matched nodes: P {p:.2f} R {rc:.2f} F1 {f:.2f} (TP {tp} FP {fp} FN {fn}); recall vs all {ga} GT edges: {tp/ga:.2f}')
    for r in rad:
        print(f'\n=== node match radius {r*100:.0f}% of image width')
        allt=[0,0,0]
        for cls in SEM:
            tp,fp,fn=tot[r][cls]; p,rc,f=prf(tp,fp,fn); print(f'{cls:14s} GT {tp+fn:4d} ours {tp+fp:4d}  P {p:.2f} R {rc:.2f} F1 {f:.2f}')
            allt[0]+=tp;allt[1]+=fp;allt[2]+=fn
        p,rc,f=prf(*allt); print(f'{"ALL nodes":14s} GT {allt[0]+allt[2]:4d} ours {allt[0]+allt[1]:4d}  P {p:.2f} R {rc:.2f} F1 {f:.2f}')
        tp,fp,fn,gall,oall=etot[r]; p,rc,f=prf(tp,fp,fn)
        tp2,fp2,fn2,g2,o2=ptot[r]; p2,rc2,f2=prf(tp2,fp2,fn2)
        print(f'PROCESS edges (no instruments) among matched nodes: P {p2:.2f} R {rc2:.2f} F1 {f2:.2f} (TP {tp2} FP {fp2} FN {fn2}); recall vs all GT process edges {tp2/g2:.2f} of {g2}')
        print(f'edges among matched nodes: P {p:.2f} R {rc:.2f} F1 {f:.2f}  (TP {tp} FP {fp} FN {fn});  GT edges total {gall}, recall vs all GT edges {tp/gall:.2f}')
if __name__=='__main__': main()
