# Symbol detector (Digitize-PID) scored on PID2Graph OPEN100

YOLOv8n trained on 500 synthetic sheets (Digitize-PID, 32 symbol classes) and scored on the same 12 OPEN100 sheets
and the same node matcher as `../open100/score.py`. Node metrics only: the detector has no connectivity and no inlet/outlet class.

Result (final `best.pt`, native scale, 640px tiles, conf 0.25, match radius 4% of image width):

| Class | GT | Detected | P | R | F1 | pid-to-kg F1 |
|---|---|---|---|---|---|---|
| valve | 257 | 209 | 0.72 | 0.58 | 0.64 | 0.98 |
| instrumentation | 350 | 463 | 0.75 | 0.99 | 0.85 | 0.99 |
| equipment (merged) | 285 | 10 | 0.60 | 0.02 | 0.04 | 0.52 |

Validation on synthetic tiles: mAP50 0.994, mAP50-95 0.929 (`train_results.csv`). The gap to OPEN100 is the synthetic-to-real domain gap;
nearly all equipment (tanks, pumps) is missed because Digitize-PID's equipment classes look unlike OPEN100's.
`score_early.txt` is the epoch-1 checkpoint, kept for comparison.

Training: epoch 1 at batch 16, then 12 more epochs from that checkpoint at batch 8 (the first run stalled from memory pressure on an 8 GB Mac).
Class mapping fixed before scoring: valve C0-C13,C24; instrumentation C25-C31; equipment-like C14-C19,C21; ignored C20,C22,C23.
Not included: weights and dataset (Digitize-PID states no licence). Rebuild with `make_tiles.py`, then
`yolo detect train data=pid.yaml model=yolov8n.pt imgsz=640`.

## v2: more sheets (PID2Graph Synthetic) + tank/pump classes

Retrained (10 epochs, initialised from v1 weights) on 200 PID2Graph Synthetic sheets (valve/tank/pump boxes from the graphml; its large
'general' class dropped as unlike OPEN100's small fittings) plus Digitize-PID tiles relabelled for valve and instrument. Classes: valve, instrument, tank, pump.
Scored on the same 12 real OPEN100 sheets (never trained on); 4% radius:

| Class | GT | Detected | P | R | F1 | v1 F1 |
|---|---|---|---|---|---|---|
| valve | 257 | 394 | 0.61 | 0.93 | 0.73 | 0.64 |
| instrumentation | 350 | 293 | 0.95 | 0.79 | 0.86 | 0.85 |
| tank | 35 | 35 | 0.17 | 0.17 | 0.17 | merged equipment 0.04 |
| pump | 16 | 34 | 0.09 | 0.19 | 0.12 | merged equipment 0.04 |

Tank/pump counts are tiny, so those rows are noisy. Files: `make_tiles_v2.py`, `score_detector2.py`, `pid2.yaml`, `score_v2.txt`, `train_results_v2.csv`.

## v3: multi-scale synthetic tiles, 15 more epochs

Initialised from v2 weights; the PID2Graph Synthetic sheets are tiled at two scales (0.45 and 0.8) so tank/pump sizes vary (real OPEN100 tanks are ~3x larger in pixels than at v2's single training scale). Same classes and scorer (`score_detector2.py`). 4% radius, native scale:

| Class | GT | Detected | P | R | F1 | v2 F1 |
|---|---|---|---|---|---|---|
| valve | 257 | 311 | 0.77 | 0.93 | 0.84 | 0.73 |
| instrumentation | 350 | 358 | 0.92 | 0.95 | 0.94 | 0.86 |
| tank | 35 | 36 | 0.11 | 0.11 | 0.11 | 0.17 |
| pump | 16 | 12 | 0.17 | 0.12 | 0.14 | 0.12 |
| ALL (4 classes) | 658 | 717 | 0.80 | 0.88 | 0.84 | 0.74 |

Valve and instrumentation improved; tank and pump did not (35 and 16 GT, so changes are within noise). Synthetic val mAP50 is 0.993, so the tank/pump failure is the synthetic-to-real gap, not under-training.
Running inference at 0.5x is worse (ALL F1 0.42, `score_v3_s0.5.txt`) because valves/instruments shrink below their trained size; native scale is right.
Files: `make_tiles_v3.py`, `pid3.yaml`, `score_v3_s1.0.txt`, `score_v3_s0.5.txt`, `train_results_v3.csv`.

## v4 (fine-tuned from v3 on package/PSFS sheets + synthetic sheets)

Data: 175 urea-package and PSFS sheets (labels from `pid_rec.py`), 240 randomised synthetic sheets, a slice of v3 data; 4,870 train / 550 val tiles. 8 epochs, MPS, 1.31 h. OPEN100 is held out and never trained on. Scripts: `render_all.py`, `make_tiles_v4.py`, `train_v4.py`; scores `score_v4_s*.txt`.

OPEN100 (12 pages, node match radius 2%), all four classes:

| scale | v3 F1 | v4 F1 | v4 valve / instr / tank / pump |
|---|---|---|---|
| 0.5 | 0.41 | 0.81 | 0.68 / 0.94 / 0.56 / 0.00 |
| 1.0 | 0.83 | 0.84 | 0.86 / 0.93 / 0.27 / 0.06 |

Caveats: in-training mAP50 0.994 is on our own generated tiles and says nothing about real scans. Pumps (16 GT) are not solved; tank precision at scale 1.0 is 0.22. Weights (`v4_best.pt`, 6.5 MB) not committed.
