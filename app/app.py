import sys
import os
import threading

# Add the directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller import data_communicator, camera_controller
from processing.TPU_image_processor import TPUImageProcessor
from processing import parking_spot_detector
from scheduling import scheduler
from api.api import FastAPIApp


class Application:
    def __init__(self):
        self.input_controller = camera_controller.CameraController()
        self.image_processor = TPUImageProcessor()
        self.data_communicator = data_communicator.DataCommunicator()
        self.parking_spot_detector = None
        self.scheduler = scheduler.Scheduler()
        self.api = FastAPIApp(self.data_communicator)

    def run_cycle(self):
        image = self.input_controller.get_input()
        processed_data = self.image_processor.process_image(image)
        self.parking_spot_detector = parking_spot_detector.ParkingSpotDetector(processed_data)
        parking_spot_status = self.parking_spot_detector.detect_parking_spots()
        self.data_communicator.update_data(parking_spot_status)

    def start(self):
        api_thread = threading.Thread(target=self.api.run)
        api_thread.daemon = True
        api_thread.start()

        self.scheduler.schedule_task(30, self.run_cycle)
        self.scheduler.run()


if __name__ == "__main__":
    app = Application()
    app.start()
