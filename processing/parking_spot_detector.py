import parking_spot_status

class ParkingSpotDetector:
    def __init__(self, processed_data):
        self.processed_data = processed_data

    def detect_parking_spots(self) -> list[parking_spot_status.ParkingSpotStatus]:
        # Dummy data 
        return [
            parking_spot_status.ParkingSpotStatus(spot_id=1, status=parking_spot_status.Status.FREE, prediction="02:30:00"),
            parking_spot_status.ParkingSpotStatus(spot_id=2, status=parking_spot_status.Status.OCCUPIED, prediction="04:00:00"),
            parking_spot_status.ParkingSpotStatus(spot_id=3, status=parking_spot_status.Status.FREE, prediction="01:00:00"),
            parking_spot_status.ParkingSpotStatus(spot_id=4, status=parking_spot_status.Status.OCCUPIED, prediction="03:00:00"),
            parking_spot_status.ParkingSpotStatus(spot_id=5, status=parking_spot_status.Status.FREE, prediction="05:00:00")
        ]