from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "best.pt"

class ComponentDetector:
    def __init__(self):
        self.model = None
        if MODEL_PATH.exists():
            try:
                from ultralytics import YOLO
                self.model = YOLO(str(MODEL_PATH))
            except Exception:
                self.model = None

    def predict(self, image):
        if self.model is None:
            return []

        try:
            results = self.model.predict(source=image, verbose=False)
            detections = []
            for result in results:
                names = result.names
                if result.boxes is None:
                    continue
                for cls, conf in zip(
                    result.boxes.cls.tolist(),
                    result.boxes.conf.tolist()
                ):
                    label = names[int(cls)]
                    detections.append({
                        "label": str(label),
                        "confidence": float(conf),
                    })
            return detections
        except Exception:
            return []
