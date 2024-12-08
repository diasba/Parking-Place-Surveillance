from controller.data_communicator import DataCommunicator
from parking_spot_status import ParkingSpotStatus

def create_dummy_data():
    data_communicator = DataCommunicator()
    dummy_data = [
        ParkingSpotStatus(id=1, occupied=False, prediction="02:30:00"),
        ParkingSpotStatus(id=2, occupied=True, prediction="04:00:00"),
        ParkingSpotStatus(id=3, occupied=False, prediction="01:00:00"),
    ]
    data_communicator.update_data(dummy_data)
    return data_communicator

if __name__ == "__main__":
    create_dummy_data()