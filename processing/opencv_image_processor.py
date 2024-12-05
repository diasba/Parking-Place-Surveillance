import image_processor
import json
import numpy as np
import cv2
from processing.opencv_image_processor import OpenCVImageProcessor

class OpenCVImageProcessor(image_processor):
    def process_image(self, image: np.ndarray) -> json:
        # preprocessing: convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Convert to JSON
        image_data = {
            "shape": gray_image.shape,
            "dtype": str(gray_image.dtype)
        }
        return json.dumps(image_data)
