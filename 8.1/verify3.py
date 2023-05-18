import tesserocr
from PIL import Image

image = Image.open('code2.jpg')

path = "C:\Tesseract-OCR\\tessdata"

image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    # 0...126= 127 count
    if i < threshold:
        table.append(0)
    else:
        # 127...255 = 129 count
        table.append(1)

# table = [0,0,0,,....0,1,...1]
#        |<---127-------><---129---->|
# 在这段代码中，LUT列表中只有两个元素，表示原始像素值小于阈值127的像素点映射到新图像中的像素值为0，
# 原始像素值大于等于阈值127的像素点映射到新图像中的像素值为1
image = image.point(table, '1')
image.show()

result = tesserocr.image_to_text(image, path=path)
print(result)
