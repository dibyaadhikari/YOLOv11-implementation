from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO("path/to/custom/model")

# Export the model to ONNX format
success = model.export(format="onnx")
