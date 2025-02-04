import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import controller.data_communicator as communicator

# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ParkingSpotStatus(BaseModel):
    spot_id: int
    status: str
    prediction: str

class FastAPIApp:
    def __init__(self, data_communicator: communicator):
        self.app = FastAPI()
        self.data_communicator = data_communicator
        self.setup_routes()
        self.setup_cors()

    def setup_routes(self):
        @self.app.get('/parking_status', response_model=List[ParkingSpotStatus])
        def get_parking_status():
            data = self.data_communicator.get_data()
            logger.info("Parking Status Data: %s", data)  
            return [ParkingSpotStatus(spot_id=status.spot_id, status=status.status.name, prediction=status.prediction) for status in data]

    def setup_cors(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def run(self):
        import uvicorn
        uvicorn.run(self.app, host='0.0.0.0', port=8001)

if __name__ == "__main__":
    data_communicator = communicator.DataCommunicator()
    app = FastAPIApp(data_communicator)
    app.run()