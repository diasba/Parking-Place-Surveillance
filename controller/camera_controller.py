import threading
import time
import io
from picamera2 import Picamera2
from PIL import Image
from controller import input_controller

class CameraController(input_controller.InputController):
    def __init__(self):
        self.camera = Picamera2()
        self.camera.configure(self.camera.create_still_configuration())  # Kamera konfigurieren
        self.current_image = None
        self.lock = threading.Lock()
        self.refresh_image()

    def refresh_image(self):
        def update_image():
            while True:
                stream = io.BytesIO()
                self.camera.capture_file('test1.jpg')  # Bild aufnehmen
                stream.seek(0)
                image = Image.open(stream)
                cropped_image = self.crop_image(image)  # Bild zuschneiden, falls benötigt
                with self.lock:
                    self.current_image = image  # Oder cropped_image, wenn zugeschnitten
                time.sleep(30)  # Wartezeit bis zum nächsten Bild

        threading.Thread(target=update_image, daemon=True).start()

    def crop_image(self, image):
        # Definiere den Zuschnittbereich (left, upper, right, lower)
        box = (100, 100, 1820, 1700)
        return image.crop(box)

    def get_current_image(self):
        with self.lock:
            return self.current_image if self.current_image else None
    
    def get_input(self):
        return self.get_current_image()
