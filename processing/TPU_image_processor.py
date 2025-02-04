import json
import torch
from PIL import Image

class TPUImageProcessor():
    def __init__(self):
        pass
        
    
    def process_image(self, image_path) -> json:
        self.predict_from_disk(image_path)
        pass
    
    
    def predict_from_disk(self, image):
       # Load YOLOv5 model
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

        #image_path = './IMG_2.jpg'
        # image = Image.open(image_path)

        # Run inference
        results = model(image)
        # Filter results for cars only
        car_class_name = 'car'
        detected_objects = results.pandas().xyxy[0]  # Get predictions as a Pandas DataFrame
        car_detections = detected_objects[detected_objects['name'] == car_class_name]

        # Print detected cars
        print("Detected Cars:")
        print(car_detections)

        # Save detected cars to a JSON file
        car_detections_dict = car_detections.to_dict(orient='records')
        with open('car_detections.json', 'w') as json_file:
            json.dump(car_detections_dict, json_file, indent=4)

        # Draw boxes only for cars
        if not car_detections.empty:
            results.save(save_dir='outputs/detected_images')  # Save results
            print(f"Car detection results saved in 'outputs/detected_images' directory.")
        else:
            print("No cars detected.")
