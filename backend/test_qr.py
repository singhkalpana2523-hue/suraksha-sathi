from app.services.qr_service import QRService

qr = QRService()

result = qr.decode_qr("test_files/upi_qr.png")

print(result)