import glob,os,random,shutil
from PIL import Image
random.seed(11)
SCALE=0.55; T=640; STRIDE=560
def tiles(split,maxn):
    out=f'tiles/images/{split}'; lab=f'tiles/labels/{split}'
    os.makedirs(out,exist_ok=True); os.makedirs(lab,exist_ok=True)
    items=[]
    for lf in sorted(glob.glob(f'data/DigitizePID_Dataset/labels/{split}/*.txt')):
        img=lf.replace('labels','images').replace('.txt','.jpg'); items.append((img,lf))
    per=max(1,maxn//len(items)) if maxn else 10**9
    n=0
    for img,lf in items:
        im=Image.open(img).convert('L'); W,H=im.size
        im=im.resize((int(W*SCALE),int(H*SCALE)),Image.LANCZOS); w,h=im.size
        boxes=[]
        for l in open(lf):
            c,xc,yc,bw,bh=l.split(); c=int(c); xc,yc,bw,bh=[float(v) for v in (xc,yc,bw,bh)]
            boxes.append((c,(xc-bw/2)*w,(yc-bh/2)*h,(xc+bw/2)*w,(yc+bh/2)*h))
        cand=[]
        for y0 in range(0,max(1,h-T+1)+STRIDE,STRIDE):
            for x0 in range(0,max(1,w-T+1)+STRIDE,STRIDE):
                x0=min(x0,max(0,w-T)); y0=min(y0,max(0,h-T)); cand.append((x0,y0))
        cand=sorted(set(cand)); random.shuffle(cand); got=0
        for x0,y0 in cand:
            ls=[]
            for c,a,b,cx,cy in boxes:
                ia,ib,ic,id_=max(a,x0),max(b,y0),min(cx,x0+T),min(cy,y0+T)
                if ic<=ia or id_<=ib: continue
                if (ic-ia)*(id_-ib)<0.6*(cx-a)*(cy-b): continue
                ls.append(f'{c} {((ia+ic)/2-x0)/T:.6f} {((ib+id_)/2-y0)/T:.6f} {(ic-ia)/T:.6f} {(id_-ib)/T:.6f}')
            if not ls: continue
            name=f'{os.path.basename(img)[:-4]}_{x0}_{y0}'
            im.crop((x0,y0,x0+T,y0+T)).convert('RGB').save(f'{out}/{name}.jpg',quality=92)
            open(f'{lab}/{name}.txt','w').write('\n'.join(ls)); got+=1; n+=1
            if got>=per: break
    print(split,n,'tiles')
shutil.rmtree('tiles',ignore_errors=True)
tiles('train',3200); tiles('val',500)
open('pid.yaml','w').write(f"path: {os.path.abspath('tiles')}\ntrain: images/train\nval: images/val\nnames:\n"+''.join(f'  {i}: C{i}\n' for i in range(32)))
