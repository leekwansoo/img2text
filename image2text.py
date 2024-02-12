import streamlit as st
import pytesseract
#import io
from PIL import Image
#from io import BytesIO
path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
#pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
exit

def image2text(image):
    
    image = Image.open(image)
   
    text = pytesseract.image_to_string(image, lang="kor")

    cleaned_text = text.replace(" ", "")
   
    return cleaned_text
    #return out

