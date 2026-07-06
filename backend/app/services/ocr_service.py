import cv2
import easyocr


class OCRService:

    def __init__(self):
        self.reader = easyocr.Reader(
            ["en", "hi"],
            gpu=False
        )

    def extract_text(self, image_path: str):

        image = cv2.imread(image_path)

        h, w = image.shape[:2]

        if w > 1200:
            scale = 1200 / w
            image = cv2.resize(
                image,
                (1200, int(h * scale))
            )

        results = self.reader.readtext(
            image,
            detail=0,
            paragraph=True
        )

        return "\n".join(results)