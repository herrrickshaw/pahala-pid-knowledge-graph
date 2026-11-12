"""v4 detector dataset: exactly labelled rendered sheets (the 178-sheet urea package + PSFS sheets, and 240 randomised synthetic P&ID sheets) tiled to 640 px at mixed
scales with scan-like degradation, plus a slice of the v3 dataset (PID2Graph synthetic + Digitize-PID) so the fine-tune does not forget it. Classes (same as v3/OPEN100 node
labels): 0 valve, 1 instrument, 2 tank, 3 pump. Split by sheet (about 1 in 8 sheets to val), never by tile."""
import os, json, glob, random, shutil, hashlib, io
import numpy as np
from PIL import Image, ImageFilter
random.seed(11); np.random.seed(11)
T, STR = 640, 480; NAMES = ["valve", "instrument", "tank", "pump"]; CMAP = {"valve": 0, "instrumentation": 1, "tank": 2, "pump": 3}
OUT = "tiles4"; shutil.rmtree(OUT, ignore_errors=True)
for s in ("train", "val"):
    os.makedirs(f"{OUT}/images/{s}"); os.makedirs(f"{OUT}/labels/{s}")
CAP = {("pkg", "train"): 1800, ("syn", "train"): 2000, ("pkg", "val"): 150, ("syn", "val"): 150}
got = {k: 0 for k in CAP}; cls_count = {"train": [0] * 4, "val": [0] * 4}


def degrade(im):
    if random.random() < 0.3:
        im = im.filter(ImageFilter.MinFilter(3))                       # heavier lines
    if random.random() < 0.7:
        im = im.filter(ImageFilter.GaussianBlur(random.uniform(0.0, 1.1)))
    a = np.asarray(im, dtype=np.float32)
    a = (a - 128) * random.uniform(0.8, 1.05) + 128 + random.uniform(-12, 8)
    if random.random() < 0.6: a += np.random.normal(0, random.uniform(2, 9), a.shape)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGB")


def tiles(png, boxes, scale, split, src, tag):
    im = Image.open(png).convert("L"); W, H = im.size
    im = im.resize((int(W * scale), int(H * scale)), Image.LANCZOS); w, h = im.size
    bx = [(CMAP[c], x0 * scale, y0 * scale, x1 * scale, y1 * scale) for c, x0, y0, x1, y1 in boxes if c in CMAP]
    xs = list(range(0, max(w - T, 0) + 1, STR)); ys = list(range(0, max(h - T, 0) + 1, STR))
    if xs[-1] + T < w: xs.append(max(w - T, 0))
    if ys[-1] + T < h: ys.append(max(h - T, 0))
    cand = [(x, y) for y in ys for x in xs]; random.shuffle(cand)
    for x0, y0 in cand:
        if got[(src, split)] >= CAP[(src, split)]: return
        ls = []; cc = [0] * 4
        for c, a, b, cx, cy in bx:
            ia, ib, ic, id_ = max(a, x0), max(b, y0), min(cx, x0 + T), min(cy, y0 + T)
            if ic <= ia or id_ <= ib or (ic - ia) * (id_ - ib) < 0.6 * (cx - a) * (cy - b): continue
            ls.append(f"{c} {((ia + ic) / 2 - x0) / T:.6f} {((ib + id_) / 2 - y0) / T:.6f} {(ic - ia) / T:.6f} {(id_ - ib) / T:.6f}"); cc[c] += 1
        if not ls: continue
        if src == "syn" and cc[2] + cc[3] == 0 and random.random() < 0.6: continue          # favour tiles with the rare classes
        crop = im.crop((x0, y0, x0 + T, y0 + T))
        if crop.size != (T, T): c2 = Image.new("L", (T, T), 255); c2.paste(crop, (0, 0)); crop = c2
        crop = degrade(crop); n = f"{tag}_{int(scale * 100)}_{x0}_{y0}"
        crop.save(f"{OUT}/images/{split}/{n}.jpg", quality=random.randint(62, 95)); open(f"{OUT}/labels/{split}/{n}.txt", "w").write("\n".join(ls))
        got[(src, split)] += 1
        for i in range(4): cls_count[split][i] += cc[i]


for src in ("pkg", "syn"):
    labs = json.load(open(f"data_v4/{src}_labels.json"))
    keys = sorted(labs, key=int)
    for k in keys:
        if not labs[k]: continue
        split = "val" if int(hashlib.md5(f"{src}{k}".encode()).hexdigest(), 16) % 8 == 0 else "train"
        png = f"data_v4/png/{src}_s{k}.png"
        if not os.path.exists(png): continue
        for sc in ((1.0, 1.4) if src == "pkg" else (0.7, 1.0, 1.4)):
            tiles(png, labs[k], sc, split, src, f"{src}{k}")
print("tiles", got, "boxes train/val by class", cls_count)
# v3 slice
def mix(split, cap):
    fs = sorted(glob.glob(f"tiles3/labels/{split}/*.txt")); random.shuffle(fs)
    for lf in fs[:cap]:
        nm = os.path.basename(lf)[:-4]
        shutil.copy(f"tiles3/images/{split}/{nm}.jpg", f"{OUT}/images/{split}/v3_{nm}.jpg"); shutil.copy(lf, f"{OUT}/labels/{split}/v3_{nm}.txt")
mix("train", 1200); mix("val", 250)
for s in ("train", "val"): print(s, len(os.listdir(f"{OUT}/images/{s}")))
open("pid4.yaml", "w").write(f"path: {os.path.abspath(OUT)}\ntrain: images/train\nval: images/val\nnames:\n" + "".join(f"  {i}: {n}\n" for i, n in enumerate(NAMES)))
