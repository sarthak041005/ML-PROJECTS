from ultralytics import YOLO

model = YOLO("runs/detect/industrial_detector/weights/best.pt")

model.predict(
    source="dataset/images/test",
    save=True,
    conf=0.4
)