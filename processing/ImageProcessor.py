from abc import ABC, abstractmethod

class ImageProcessor(ABC):
    @abstractmethod
    def process_image(self, image: Image) -> ProcessedData:
        """Verarbeitet ein Bild und gibt die relevanten Daten zurück."""
        pass
