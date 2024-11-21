from abc import ABC, abstractmethod

class InputController(ABC):
    @abstractmethod
    def get_input(self):
        pass