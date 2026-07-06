from app.services.ocr_service import OCRService

ocr = OCRService()

text = ocr.extract_text("sample.jpg")

print(text)