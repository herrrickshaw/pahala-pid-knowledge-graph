# Run from this directory: python3 score.py
import json,collections
tot=collections.Counter(); bytype=collections.defaultdict(collections.Counter); bypage={}
fails=[]
for pg in range(9,26):
    K=json.load(open(f'key/audit_key_{pg:02d}.json')); R=json.load(open(f'result_{pg:02d}.json'))['verdicts']
    c=collections.Counter()
    for cid,k in K.items():
        v=R.get(cid,{}).get('v','missing')
        grp='true' if k['true'] else 'decoy'
        c[(grp,v)]+=1; tot[(grp,v)]+=1; bytype[(k['type'],grp)][v]+=1
        if k['true'] and v=='wrong': fails.append((pg,cid,k['type'],k['text'],R[cid]['evidence']))
        if (not k['true']) and v=='correct': fails.append((pg,cid,'DECOY-ACCEPTED',k['text'],R[cid]['evidence']))
    bypage[pg]=c
print('TOTAL',dict(tot))
for g in('true','decoy'):
    n=sum(v for (a,b),v in tot.items() if a==g); print(g,n,{b:round(v/n*100,1) for (a,b),v in tot.items() if a==g})
print('--by type (true claims)')
for (t,g),c in sorted(bytype.items()):
    if g=='true':
        n=sum(c.values()); print(t,n,dict(c),'agree %.0f%%'%(100*c['correct']/n))
print('--by type (decoys)')
for (t,g),c in sorted(bytype.items()):
    if g=='decoy': print(t,sum(c.values()),dict(c))
print('--by page true correct%')
for pg,c in bypage.items():
    n=sum(v for (g,_),v in c.items() if g=='true'); print(pg,n,'%.0f%%'%(100*c[('true','correct')]/n), 'decoy rejected', c[('decoy','wrong')],'/',sum(v for (g,_),v in c.items() if g=='decoy'))
json.dump(fails,open('disagreements.json','w'),indent=1)
print(len(fails),'disagreements')
