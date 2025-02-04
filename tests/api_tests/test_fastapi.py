import pytest
from fastapi.middleware.cors import CORSMiddleware
from api.api import FastAPIApp
import controller.data_communicator as communicator
from unittest.mock import patch

class Test_Fast_API_App:
    def setup_method(self):
        data_communicator = communicator.DataCommunicator()
        self.app_instance = FastAPIApp(data_communicator)

    def test_init(self):
        assert self.app_instance is not None

    # ensure route is setup
    def test_setup_routes(self):
        self.app_instance.setup_routes()
        routes = [route.path for route in self.app_instance.app.routes]
        assert '/parking_status' in routes
        
    # ensure cors is setup
    def test_setup_cors(self):
        with patch.object(self.app_instance.app, 'add_middleware', wraps=self.app_instance.app.add_middleware) as mock_add_middleware:
            self.app_instance.setup_cors()
            mock_add_middleware.assert_called_once_with(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

    def test_run(self):
        with patch('uvicorn.run') as mock_run:
            try:
                self.app_instance.run()
                mock_run.assert_called_once_with(self.app_instance.app, host='0.0.0.0', port=8001)
            except Exception as e:
                pytest.fail(f"test_run raised an exception: {e}")