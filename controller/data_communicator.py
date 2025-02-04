import parking_spot_status
from parking_spot_status import ParkingSpotStatus, Status
import threading
from PIL import Image
import json

class DataCommunicator:
    def __init__(self):
        self.parking_spot_status = []
        self.lock = threading.Lock()

    def update_data(self, parking_spot_status: list[parking_spot_status.ParkingSpotStatus]) -> None:
        with self.lock:
            self.parking_spot_status = parking_spot_status

    def get_data(self) -> list[parking_spot_status.ParkingSpotStatus]:
        self.parking_spot_status = self.get_dummy_data()
        with self.lock:
            return self.parking_spot_status.copy()
    def get_dummy_data(self) -> list[parking_spot_status.ParkingSpotStatus]:
        with open('controller/dummy_data.json', 'r') as f:
            data = json.load(f)
            parking_spots = [ParkingSpotStatus(spot['spot_id'], Status[spot['status']], spot['prediction']) for spot in data]
        return parking_spots
        
    # def get_data(self, img_path):
    #    with self.lock:
    #        image = Image.open(img_path)
    #        return image