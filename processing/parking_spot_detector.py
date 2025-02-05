import parking_spot_status


class ParkingSpotDetector:
    def __init__(self, processed_data):
        self.processed_data = processed_data

    def detect_parking_spots(self) -> list[parking_spot_status.ParkingSpotStatus]:
        # Process the real data to detect parking spots
        parking_spot_statuses = []
        for spot in self.processed_data:
            spot_status = parking_spot_status.ParkingSpotStatus(
                spot_id=spot['spot_id'],
                status=parking_spot_status.Status[spot['status']],
                prediction=spot['prediction']
            )
            parking_spot_statuses.append(spot_status)
        return parking_spot_statuses
