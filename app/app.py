import sys
import os
import threading

# Füge das Verzeichnis zum Python-Pfad hinzu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller import camera_controller, data_communicator
from processing.dummy_image_processor import DummyImageProcessor
from processing import TPU_image_processor
from processing import parking_spot_detector
from scheduling import scheduler
from api import fastapi
path = ''

class Application:
    def __init__(self):
        # self.input_controller = camera_controller.CameraController()
        self.image_processor = TPU_image_processor()
        self.data_communicator = data_communicator.DataCommunicator()
        self.parking_spot_detector = None
        self.scheduler = scheduler.Scheduler()
        self.api = fastapi.FastAPIApp(self.data_communicator)

    def run_cycle(self):
        # image = self.input_controller.get_input()
        image = self.data_communicator.get_data(img_path=path)
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