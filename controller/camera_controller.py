import threading
import time
import io
from picamera2 import Picamera2
from PIL import Image
from controller import input_controller

class CameraController(input_controller.InputController):
    def __init__(self):
        self.camera = Picamera2()
        self.camera.configure(self.camera.create_still_configuration())  # Configure camera
        self.current_image = None
        self.lock = threading.Lock()
        self.refresh_image()

    def refresh_image(self):
        def update_image():
            while True:
                stream = io.BytesIO()
                self.camera.capture_file(stream, format='jpeg')  # Capture image directly to stream
                stream.seek(0)
                image = Image.open(stream)
                cropped_image = self.crop_image(image)  # Crop image if needed
                with self.lock:
                    self.current_image = cropped_image  # Use cropped_image if cropped
                time.sleep(30)  # Wait time until next image

        threading.Thread(target=update_image, daemon=True).start()

    def crop_image(self, image):
        # Define the crop area (left, upper, right, lower)
        box = (1820, 2820, 2991, 3563)
        return image.crop(box)

    def get_current_image(self):
        with self.lock:
            return self.current_image if self.current_image else None

    def get_input(self):
        return self.get_current_image()