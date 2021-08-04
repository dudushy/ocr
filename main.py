# imports
from PIL import Image
from pytesseract import *
import glob

# init
pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# main 1
img = Image.open(r'ocr\input\demo.png')
output = pytesseract.image_to_string(img)

print(output)

with open(r'ocr\output\demo.txt', 'w', encoding='utf-8') as result:
    result.write(output)

# main 2
try:                       #0123456789-4321
    for img in glob.iglob(r'ocr\input\*.png'):
        with open(r'ocr\output\test.txt', 'a', encoding='utf-8') as output:
            output.write(pytesseract.image_to_string(img))
except Exception as e:
    print('\n' + e)