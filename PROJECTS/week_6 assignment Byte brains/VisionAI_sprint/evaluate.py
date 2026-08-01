from ultralytics import YOLO

model = YOLO("runs/detect/industrial_detector/weights/best.pt")

metrics = model.val()

print(metrics)