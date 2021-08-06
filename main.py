# imports
from pytesseract import *
import glob

# init
pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# main 2
try:                       #0123456789-4321
    for img in glob.iglob(r'ocr\input\*.png'):
        output = pytesseract.image_to_string(img)
        print("= = = = = = = = = = = = = = = = = = = = =")
        print(f'{img[10:]}: {output}')
        with open(rf'ocr\output\{img[10:-4]}.txt', 'w', encoding='utf-8') as result:
            result.write(output)
    print("= = = = = = = = = = = = = = = = = = = = =")
except Exception as e:
    print('\n' + e)