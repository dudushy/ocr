# imports
from PIL import Image
from pytesseract import *

# init
pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# vars
img = Image.open(r'ocr\input\demo.png')
output = pytesseract.image_to_string(img)

print(output)

with open(r'ocr\output\demo.txt', 'w', encoding='utf-8') as result:
    result.write(output)