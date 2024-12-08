import json
from processing.image_processor import ImageProcessor

class DummyImageProcessor(ImageProcessor):
    def process_image(self, image) -> json:
        # Processing of dummy data
        return json.dumps({"dummy_key": "dummy_value"})