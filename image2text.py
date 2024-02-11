import pytesseract
import io
img_file = "text1.png"
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

def image2text(img_file):
           
    image = Image.open(img_file)
   
    text = pytesseract.image_to_string(image, lang="kor")

    cleaned_text = text.replace(" ", "")
   
    return cleaned_text
    #return out

