"""Fine-tune the v3 detector (PID2Graph synthetic + Digitize-PID) on exactly labelled urea-package / PSFS sheets and randomised synthetic sheets (pid4.yaml)."""
from ultralytics import YOLO
m = YOLO("v3_best.pt")
m.train(data="pid4.yaml", epochs=8, imgsz=640, batch=8, device="mps", workers=0, lr0=0.003, lrf=0.1, patience=5, plots=False, project="runs", name="pid_v4", exist_ok=True,
        scale=0.6, degrees=0.0, fliplr=0.5, mosaic=1.0, close_mosaic=2, amp=False, seed=0, deterministic=True)
