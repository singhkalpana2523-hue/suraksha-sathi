import cv2
from pyzbar.pyzbar import decode


class QRService:

    def decode_qr(self, image_path: str):

        image = cv2.imread(image_path)

        decoded = decode(image)

        if not decoded:
            return None

        qr = decoded[0]

        content = qr.data.decode("utf-8")

        return {
            "content": content,
            "qr_type": self.classify_qr(content)
        }

    def classify_qr(self, content: str):

        if content.startswith("upi://"):
            return "UPI"

        elif content.startswith("http://") or content.startswith("https://"):
            return "URL"

        elif content.startswith("WIFI:"):
            return "WIFI"

        elif content.startswith("BEGIN:VCARD"):
            return "CONTACT"

        else:
            return "TEXT"