import json
from abc import ABC, abstractmethod

class ImageProcessor(ABC):
    @abstractmethod
    def process_image(self, image) -> json:
         # Processing of dummy data
        return json.dumps({"dummy_key": "dummy_value"})