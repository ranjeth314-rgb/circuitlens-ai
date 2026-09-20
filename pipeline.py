from pathlib import Path
import numpy as np

from .detector import ComponentDetector
from .ocr import OCRReader
from .knowledge import COMPONENT_KNOWLEDGE


class CircuitLensPipeline:
    def __init__(self):
        self.detector = ComponentDetector()
        self.ocr = OCRReader()

    def analyze(self, image):
        detections = self.detector.predict(image)
        ocr_text = self.ocr.read(image)
        return {
            "detections": detections,
            "ocr_text": ocr_text,
        }

    def knowledge(self, label):
        return COMPONENT_KNOWLEDGE.get(
            label.lower(),
            {
                "function": "Information not available in the local knowledge base.",
                "checks": "Verify the component identity and consult its datasheet.",
                "troubleshooting": "Inspect orientation, connections, power conditions and component ratings."
            },
        )
