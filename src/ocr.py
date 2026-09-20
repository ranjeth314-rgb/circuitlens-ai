import os

class OCRReader:
    def __init__(self):
        self.enabled = False
        try:
            import pytesseract
            self.pytesseract = pytesseract
            cmd = os.getenv("TESSERACT_CMD")
            if cmd:
                self.pytesseract.pytesseract.tesseract_cmd = cmd
            self.enabled = True
        except Exception:
            pass

    def read(self, image):
        if not self.enabled:
            return ""

        try:
            text = self.pytesseract.image_to_string(image)
            return text.strip()
        except Exception:
            return ""
