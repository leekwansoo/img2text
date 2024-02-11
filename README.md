## https://www.youtube.com/watch?v=rNxMwtottmM&t=21s

download "Tesseract-OCR" and  install it in your Program Files Folder

when installing check the korean language in foreign language option.

include the following statment in the image2text.py file

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
