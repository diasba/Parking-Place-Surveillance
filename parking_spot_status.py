from enum import Enum

class Status(Enum):
    FREE = 1
    OCCUPIED = 2

class ParkingSpotStatus:
    def __init__(self, spot_id: int, status: Status, prediction: str):
        self.spot_id = spot_id
        self.status = status
        self.prediction = prediction

    def to_dict(self):
        return {
            'spot_id': self.spot_id,
            'status': self.status.name,
            'prediction': self.prediction
        }