from yolo_detection import load_image, detect_objects
from text_generation import generate_text

def main(img_path):
    # Load the image
    image = load_image(img_path)

    # Detect objects
    objects = detect_objects(image)
    print("Detected Objects:", objects)

    # Generate text based on detected objects
    generated_text = generate_text(objects)
    print("Generated Text:", generated_text)

if __name__ == "__main__":
    img_path = 'image\dog_bike_car.jpg'  # Replace with your image path
    main(img_path)
