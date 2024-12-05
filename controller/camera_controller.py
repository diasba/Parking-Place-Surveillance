import numpy as np
import input_controller
from picamera import PiCamera
import cv2
import io


class CameraController(input_controller):
    def __init__(self):
        self.camera = PiCamera()
        # Config for cam
        #        camera.resolution = (x, y)
        #        camera.vflip = True
        #        camera.contrast = 10
        #        camera.image_effect = "watercolor"
        self.running = False

    def get_input(self):  # return image as a ndarray
        self.camera.start_preview()
        #       sleep(2)
        stream = io.BytesIO()
        self.camera.capture(stream, format='jpeg')
        self.camera.stop_preview()
        stream.truncate()
        stream.seek(0)
        image = np.frombuffer(stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # Cropping
        x, y, w, h = 100, 100, 200, 200
        cropped_image = image[y:y+h, x:x+w]

        # Save the cropped image
        #  cv2.imwrite('/tmp/cropped_image.jpg', cropped_image)
        return cropped_image
