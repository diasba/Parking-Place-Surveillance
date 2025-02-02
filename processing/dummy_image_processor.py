import json
import threading
import time
import numpy as np
from datetime import datetime
from processing.image_processor import ImageProcessor
from controller.camera_controller import CameraController
from processing.opencv_image_processor import OpenCVImageProcessor


class DummyImageProcessor(ImageProcessor):
    def __init__(self):
        self.camera_controller = CameraController()
        self.opencv_processor = OpenCVImageProcessor()
        self.start_saving_images()

    def process_image(self, image) -> json:
        # Processing of dummy data
        return json.dumps({"dummy_key": "dummy_value"})

    def save_image_with_timestamp(self):
        while True:
            image = self.camera_controller.get_current_image()
            if image:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                image.save(f"/home/{timestamp}.jpg")

                # Process the image using OpenCVImageProcessor
                image_np = np.array(image)
                processed_json = self.opencv_processor.process_image(image_np)

                # Save the JSON output
                with open(f"/home/{timestamp}.json", 'w') as json_file:
                    json_file.write(processed_json)

            time.sleep(10)

    def start_saving_images(self):
        threading.Thread(target=self.save_image_with_timestamp, daemon=True).start()