import tesserocr
from PIL import Image

image = Image.open('code2.jpg')
result = tesserocr.image_to_text(image, path="C:\Tesseract-OCR\\tessdata")
print(result)
# PFRL