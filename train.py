from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO("yolo11n.yaml")

#Train the model with our custom dataset for 50 epochs
results = model.train(data="path/to/custom.yaml", epochs=50, batch=64, imgsz=256)
