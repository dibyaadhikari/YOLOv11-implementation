from ultralytics import YOLO
import cv2
# Create a new YOLO model from scratch
model = YOLO("path/to/custom/model")


image = cv2.imread("/path/to/image")
# Perform object detection on an image using the model

results = model.predict("path/to/image", save=True, imgsz=256, conf=0.5)

# Extract bounding boxes
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())  # Bounding box coordinates

        # Draw bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 1)  # Green box

        # Draw label "app" on top of the bounding box
        label = "char"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, label, (x1, y1 - 5), font, 0.4, (255, 255, 255), 1, cv2.LINE_AA)  # White text

# Display the image with bounding boxes and "app" label
cv2.imshow("YOLOv11 Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
