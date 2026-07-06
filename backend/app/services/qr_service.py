import cv2

class QRService:

    def decode_qr(self, image_path):
        detector = cv2.QRCodeDetector()

        image = cv2.imread(image_path)

        data, points, _ = detector.detectAndDecode(image)

        if not data:
            return None

        return {
            "content": data,
            "qr_type": "QR"
        }