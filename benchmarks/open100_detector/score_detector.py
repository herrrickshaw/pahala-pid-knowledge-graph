"""Run the Digitize-PID-trained YOLO detector on PID2Graph OPEN100 sheets and score nodes
with the same matcher as work/open100_score/score.py.
Usage: python score_detector.py <weights.pt> <gt_dir> [scale] [conf]
Class mapping fixed before any result was seen:
  valve = C0-C13, C24 ; instrumentation = C25-C31 ; equipment-like = C14-C19, C21 ; ignored = C20, C22, C23
The detector has no inlet/outlet class and produces no connectivity, so only node metrics are reported."""
import sys, os, json, collections
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'open100'))
import score as S
from PIL import Image
from ultralytics import YOLO
import torch, torchvision

VALVE = set(list(range(0, 14)) + [24]); INSTR = set(range(25, 32)); EQUIP = set(list(range(14, 20)) + [21])
def cls_of(c): return 'valve' if c in VALVE else 'instrumentation' if c in INSTR else 'general' if c in EQUIP else None

def detect(model, img, scale, conf, T=640, overlap=160):
    W, H = img.size
    im = img.resize((int(W * scale), int(H * scale)), Image.BILINEAR) if scale != 1 else img
    w, h = im.size; step = T - overlap
    xs = list(range(0, max(w - T, 0) + 1, step)); ys = list(range(0, max(h - T, 0) + 1, step))
    if xs[-1] + T < w: xs.append(w - T)
    if ys[-1] + T < h: ys.append(h - T)
    boxes, scores, cls = [], [], []
    for y in ys:
        for x in xs:
            tile = im.crop((x, y, min(x + T, w), min(y + T, h)))
            r = model.predict(tile, imgsz=T, conf=conf, device='cpu', verbose=False)[0]
            for b, s, c in zip(r.boxes.xyxy.tolist(), r.boxes.conf.tolist(), r.boxes.cls.tolist()):
                boxes.append([b[0] + x, b[1] + y, b[2] + x, b[3] + y]); scores.append(s); cls.append(int(c))
    if not boxes: return []
    bt = torch.tensor(boxes); st = torch.tensor(scores); ct = torch.tensor(cls)
    keep = torchvision.ops.batched_nms(bt, st, ct, 0.5).tolist()
    return [(boxes[i], scores[i], cls[i]) for i in keep]  # coords in scaled-image px

def main():
    wts, gtd = sys.argv[1], sys.argv[2]
    scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0; conf = float(sys.argv[4]) if len(sys.argv) > 4 else 0.25
    model = YOLO(wts); rad = [0.01, 0.02, 0.04]
    tot = {r: collections.defaultdict(lambda: [0, 0, 0]) for r in rad}; ndet = collections.Counter()
    for pg in range(12):
        img = Image.open(os.path.join(gtd, f'{pg}.png')).convert('RGB'); W, H = img.size
        dets = detect(model, img, scale, conf); items = {}
        for i, (b, s, c) in enumerate(dets):
            k = cls_of(c)
            if k is None: continue
            ndet[k] += 1
            items[f'd{i}'] = {'cls': k, 'bbox': [b[0] / scale / W, b[1] / scale / H, b[2] / scale / W, b[3] / scale / H]}
        gsem, _ = S.load_gt(os.path.join(gtd, f'{pg}.graphml'))
        for r in rad:
            m = S.match(gsem, items, W, H, r, coarse=True)
            for cls, gl in (('valve', ('valve',)), ('instrumentation', ('instrumentation',)), ('equipment', ('tank', 'pump', 'general'))):
                gn = [n for n, d in gsem.items() if d['label'] in gl]
                on = [o for o, it in items.items() if S.COARSE.get(it['cls'], it['cls']) == cls]
                tp = sum(1 for o in on if o in m)
                t = tot[r][cls]; t[0] += tp; t[1] += len(on) - tp; t[2] += len(gn) - tp
        print('page', pg + 1, 'dets', len(dets), flush=True)
    print('detections kept by class:', dict(ndet), '| weights:', wts, '| scale', scale, 'conf', conf)
    for r in rad:
        print(f'\n=== node match radius {r*100:.0f}% of image width')
        allt = [0, 0, 0]
        for cls in ('valve', 'instrumentation', 'equipment'):
            tp, fp, fn = tot[r][cls]; p, rc, f = S.prf(tp, fp, fn)
            print(f'{cls:16s} GT {tp+fn:4d} ours {tp+fp:4d}  P {p:.2f} R {rc:.2f} F1 {f:.2f}')
            allt[0] += tp; allt[1] += fp; allt[2] += fn
        p, rc, f = S.prf(*allt); print(f'{"ALL (3 classes)":16s} GT {allt[0]+allt[2]:4d} ours {allt[0]+allt[1]:4d}  P {p:.2f} R {rc:.2f} F1 {f:.2f}')
if __name__ == '__main__': main()
