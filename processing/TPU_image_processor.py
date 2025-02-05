import json
import torch
from PIL import Image

class TPUImageProcessor():
    def __init__(self):
        pass

    def process_image(self, image: Image) -> json:
        coordinates = self.predict_from_disk(image)
        pre_set_coordinates = [
            {'spot_id': 1, 'xmin': 200, 'ymin': 170, 'xmax': 210, 'ymax': 185},
            {'spot_id': 2, 'xmin': 280, 'ymin': 340, 'xmax': 290, 'ymax': 355},
            {'spot_id': 3, 'xmin': 560, 'ymin': 540, 'xmax': 570, 'ymax': 550}
        ]
        overlaps = self.check_overlaps(coordinates, pre_set_coordinates)

        result = []
        for pre_set in pre_set_coordinates:
            status = 'OCCUPIED' if any(overlap['pre_set'] == pre_set for overlap in overlaps) else 'FREE'
            result.append({
                'spot_id': pre_set['spot_id'],
                'status': status,
                'prediction': 0
            })

        return json.dumps(result, indent=4)

    def predict_from_disk(self, image):
        # Load YOLOv5 model
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

        # Run inference
        results = model(image)
        # Filter results for cars and trucks only
        car_class_name = 'car'
        truck_class_name = 'truck'
        detected_objects = results.pandas().xyxy[0]  # Get predictions as a Pandas DataFrame
        car_detections = detected_objects[
            (detected_objects['name'] == car_class_name) | (detected_objects['name'] == truck_class_name)]

        # Extract coordinates
        coordinates = car_detections[['xmin', 'ymin', 'xmax', 'ymax']].to_dict(orient='records')

        # Print detected car coordinates
        print("Detected Car Coordinates:")
        print(coordinates)

        return coordinates

    def check_overlaps(self, detected_coords, pre_set_coords):
        def is_overlapping(box1, box2):
            return not (box1['xmax'] < box2['xmin'] or box1['xmin'] > box2['xmax'] or
                        box1['ymax'] < box2['ymin'] or box1['ymin'] > box2['ymax'])

        overlaps = []
        for detected in detected_coords:
            for pre_set in pre_set_coords:
                if is_overlapping(detected, pre_set):
                    overlaps.append({'detected': detected, 'pre_set': pre_set})
        return overlaps