from ultralytics import YOLO
import cv2

def load_image(img_path):
    """Loads an image from the specified path."""
    return cv2.imread(img_path)

def detect_objects(image, confidence_threshold=0.5):
    """Detects objects in the given image using YOLOv8 and filters based on confidence."""
    # Load YOLOv8 model (load once if possible to improve performance)
    model = YOLO('yolov8n.pt')

    # Run inference
    results = model(image)

    # Initialize list for detected objects
    objects = []

    # Process results
    for result in results:
        # Get the detection boxes and their attributes
        boxes = result.boxes
        for box in boxes:
            # Check the confidence score
            if box.conf > confidence_threshold:
                # Append the object label to the list
                object_label = result.names[int(box.cls)]
                objects.append(object_label)

    # Return unique object labels
    return list(set(objects))  # Removing duplicates


