import image_processor
import json
import torch
from PIL import Image

class TPUImageProcessor(image_processor):
    def __init__(self):
        pass
        
    
    def process_image(self, image: Image) -> json:
        self.predict()
        pass
    
    
    def predict(image):
       

        # Load YOLOv5 model
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

        # Run inference
        results = model(image)
        # Filter results for cars only
        car_class_name = 'car'
        detected_objects = results.pandas().xyxy[0]  # Get predictions as a Pandas DataFrame
        car_detections = detected_objects[detected_objects['name'] == car_class_name]

        # Print detected cars
        print("Detected Cars:")
        print(car_detections)

        # Draw boxes only for cars
        if not car_detections.empty:
            results.save(save_dir='outputs/detected_images')  # Save results
            print(f"Car detection results saved in 'outputs/detected_images' directory.")
        else:
            print("No cars detected.")
