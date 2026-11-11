"""Combined detector dataset: PID2Graph Synthetic (valve/tank/pump, real node bboxes) + Digitize-PID tiles relabelled
(valve classes -> valve, C25-31 -> instrument). Classes: 0 valve, 1 instrument, 2 tank, 3 pump.
PID2Graph Synthetic has no instruments or inlet/outlet; its 'general' class is large and unlike OPEN100's small fittings, so it is dropped."""
import os,random,shutil,glob
import networkx as nx
from PIL import Image
random.seed(5); Image.MAX_IMAGE_PIXELS=None
SC=0.45; T=640; STR=560; SYN='../pid2graph_data/synthetic'
NAMES=['valve','instrument','tank','pump']; MAP={'valve':0,'tank':2,'pump':3}
OUT='tiles2'; shutil.rmtree(OUT,ignore_errors=True)
for s in('train','val'):
    os.makedirs(f'{OUT}/images/{s}'); os.makedirs(f'{OUT}/labels/{s}')
def syn(i,split,cap):
    g=nx.read_graphml(f'{SYN}/{i}.graphml'); im=Image.open(f'{SYN}/{i}.jpg').convert('L'); W,H=im.size
    im=im.resize((int(W*SC),int(H*SC)),Image.LANCZOS); w,h=im.size
    bx=[(MAP[a['label']],float(a['xmin'])*SC,float(a['ymin'])*SC,float(a['xmax'])*SC,float(a['ymax'])*SC) for _,a in g.nodes(data=True) if a['label'] in MAP]
    cand=[(min(x,max(0,w-T)),min(y,max(0,h-T))) for y in range(0,h,STR) for x in range(0,w,STR)]; cand=sorted(set(cand)); random.shuffle(cand); got=0
    for x0,y0 in cand:
        ls=[]
        for c,a,b,cx,cy in bx:
            ia,ib,ic,id_=max(a,x0),max(b,y0),min(cx,x0+T),min(cy,y0+T)
            if ic<=ia or id_<=ib or (ic-ia)*(id_-ib)<0.6*(cx-a)*(cy-b): continue
            ls.append(f'{c} {((ia+ic)/2-x0)/T:.6f} {((ib+id_)/2-y0)/T:.6f} {(ic-ia)/T:.6f} {(id_-ib)/T:.6f}')
        if not ls: continue
        n=f'syn{i}_{x0}_{y0}'; im.crop((x0,y0,x0+T,y0+T)).convert('RGB').save(f'{OUT}/images/{split}/{n}.jpg',quality=92)
        open(f'{OUT}/labels/{split}/{n}.txt','w').write('\n'.join(ls)); got+=1
        if got>=cap: break
    return got
def dig(split,cap):
    fs=sorted(glob.glob(f'tiles/labels/{split}/*.txt')); random.shuffle(fs); n=0
    for lf in fs:
        ls=[]
        for l in open(lf):
            c,*r=l.split(); c=int(c); k=0 if (c<=13 or c==24) else 1 if c>=25 else None
            if k is not None: ls.append(' '.join([str(k)]+r))
        if not ls: continue
        nm=os.path.basename(lf)[:-4]; shutil.copy(f'tiles/images/{split}/{nm}.jpg',f'{OUT}/images/{split}/dig_{nm}.jpg')
        open(f'{OUT}/labels/{split}/dig_{nm}.txt','w').write('\n'.join(ls)); n+=1
        if n>=cap: break
    return n
a=sum(syn(i,'train',12) for i in range(200)); b=sum(syn(i,'val',6) for i in range(200,250))
c=dig('train',1700); d=dig('val',250); print('syn',a,b,'dig',c,d)
open('pid2.yaml','w').write(f"path: {os.path.abspath(OUT)}\ntrain: images/train\nval: images/val\nnames:\n"+''.join(f'  {i}: {n}\n' for i,n in enumerate(NAMES)))
