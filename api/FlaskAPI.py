from flask import Flask, jsonify
import threading

class FlaskAPI:
    def __init__(self, data_communicator: DataCommunicator):
        self.app = Flask(__name__)
        self.data_communicator = data_communicator
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/parking_status', methods=['GET'])
        def get_parking_status():
            data = self.data_communicator.get_data()
            return jsonify([status.to_dict() for status in data])

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)
