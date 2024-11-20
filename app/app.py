import threading
from controller import CameraController
from processing import ImageProcessor
from processing import ParkingSpotDetector
from scheduling import Scheduler
from api import FlaskAPI, DataCommunicator


class Application:
    def __init__(self, image_processor: ImageProcessor):
        self.camera_controller = CameraController()
        self.image_processor = image_processor
        self.data_communicator = DataCommunicator()
        self.parking_spot_detector = None
        self.scheduler = Scheduler()
        self.api = FlaskAPI(self.data_communicator)

    def run_cycle(self):
        image = self.camera_controller.capture_image()
        processed_data = self.image_processor.process_image(image)
        self.parking_spot_detector = ParkingSpotDetector(processed_data)
        parking_spot_status = self.parking_spot_detector.detect_parking_spots()
        self.data_communicator.update_data(parking_spot_status)

    def start(self):
        api_thread = threading.Thread(target=self.api.run)
        api_thread.daemon = True
        api_thread.start()

        self.scheduler.schedule_task(30, self.run_cycle)
        self.scheduler.run()
