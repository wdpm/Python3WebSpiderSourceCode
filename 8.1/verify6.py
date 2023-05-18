import numpy as np
import tesserocr
from PIL import Image

image = Image.open('captcha2.png')
image = image.convert('L')
threshold = 50
array = np.array(image)
array = np.where(array > threshold, 255, 0)
image = Image.fromarray(array.astype('uint8'))
text = tesserocr.image_to_text(image, path="C:\Tesseract-OCR\\tessdata")
print(text)
