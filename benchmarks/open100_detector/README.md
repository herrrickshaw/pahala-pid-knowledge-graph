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
