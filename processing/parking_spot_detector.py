import parking_spot_status

class ParkingSpotDetector:
    def __init__(self, processed_data: ProcessedData):
        self.processed_data = processed_data

    def detect_parking_spots(self) -> list[parking_spot_status.ParkingSpotStatus]:
        pass
