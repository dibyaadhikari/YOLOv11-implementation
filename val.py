from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO("path/to/custom/model")

# Evaluate the model's performance on the validation set
results = model.val()

