import parking_spot_status
import threading
from PIL import Image

class DataCommunicator:
    def __init__(self):
        self.parking_spot_status = []
        self.lock = threading.Lock()

    def update_data(self, parking_spot_status: list[parking_spot_status.ParkingSpotStatus]) -> None:
        with self.lock:
            self.parking_spot_status = parking_spot_status

    def get_data(self) -> list[parking_spot_status.ParkingSpotStatus]:
        with self.lock:
            return self.parking_spot_status.copy()
        
    def get_data(self, img_path):
        with self.lock:
            image = Image.open(img_path)
            return image