import threading
from controller import camera_controller, data_communicator
from processing import image_processor
from processing import parking_spot_detector
from scheduling import scheduler
from api import flask_api


class Application:
    def __init__(self, processor: image_processor.ImageProcessor):
        self.input_controller = camera_controller.CameraController()
        self.image_processor = processor
        self.data_communicator = data_communicator.DataCommunicator()
        self.parking_spot_detector = None
        self.scheduler = scheduler.Scheduler()
        self.api = flask_api.FlaskAPI(self.data_communicator)

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
