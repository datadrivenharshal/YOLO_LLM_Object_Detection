from ultralytics import YOLO
import cv2

def load_image(img_path):
    """Loads an image from the specified path."""
    return cv2.imread(img_path)

def detect_objects(image):
    """Detects objects in the given image using YOLOv8."""
    model = YOLO('yolov8n.pt')
    results = model(image)
    objects = results[0].names
    return objects
