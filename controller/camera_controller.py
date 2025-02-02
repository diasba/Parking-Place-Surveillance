import threading
import time
import io
import picamera
from PIL import Image


from controller import input_controller

class CameraController(input_controller.InputController):
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1920, 1080)
        self.current_image = None
        self.lock = threading.Lock()
        self.refresh_image()

    def refresh_image(self):
        def update_image():
            while True:
                stream = io.BytesIO()
                self.camera.capture(stream, format='jpeg')
                stream.seek(0)
                image = Image.open(stream)
                cropped_image = self.crop_image(image)
                with self.lock:
                    self.current_image = image
                    # self.current_image = cropped_image # Uncomment this line to crop the image
                time.sleep(30)

        threading.Thread(target=update_image, daemon=True).start()

    def crop_image(self, image):
        # Define the cropping box (left, upper, right, lower)
        box = (100, 100, 1820, 1700)
        return image.crop(box)

    def get_current_image(self):
        with self.lock:
            return self.current_image