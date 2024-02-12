import streamlit as st
import pytesseract
#import io
from PIL import Image
#from io import BytesIO
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
#pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
exit

def image2text(image):
    
    image = Image.open(image)
   
    text = pytesseract.image_to_string(image, lang="kor")

    cleaned_text = text.replace(" ", "")
   
    return cleaned_text
    #return out

