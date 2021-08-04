# imports
from PIL import Image
from pytesseract import *
import glob

# init
pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# main 2
try:                       #0123456789-4321
    for img in glob.iglob(r'ocr\input\*.png'):
        print(f'\n{img}')
        output = pytesseract.image_to_string(img)
        print(f'\n{output}')
        with open(r'ocr\output\test.txt', 'a', encoding='utf-8') as result:
            result.write(output)
        print(f'\nNEXT')
except Exception as e:
    print('\n' + e)