import json
import numpy as np
import cv2
import torch
from processing.image_processor import ImageProcessor


class OpenCVImageProcessor(ImageProcessor):
    def process_image(self, image: np.ndarray) -> json:
        # Preprocessing: convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Normalize the image
        normalized_image = gray_image / 255.0

        # Convert to Torch tensor
        tensor_image = torch.tensor(normalized_image, dtype=torch.float32)

        # Add batch dimension and channel dimension
        tensor_image = tensor_image.unsqueeze(0).unsqueeze(0)

        # Convert to JSON
        image_data = {
            "shape": tensor_image.shape,
            "dtype": str(tensor_image.dtype)
        }
        return json.dumps(image_data)