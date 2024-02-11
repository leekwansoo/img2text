import streamlit as st 
from image2text import image2text
import os


st.title("Image to Text Converter")
st.sidebar.title("Select Image to convert")

image = st.sidebar.file_uploader(label= "Upload a Image", type = ["jpg", "jpeg", "png"])

file_name = st.sidebar.text_input(label = "Enter Output File Name")

if image is not None:
    st.image(image)

st.markdown("""
            ### Abstracted Text
            <hr>
            """,True)
result = image2text(image)
st.text(result)
st.download_button(label="download text", data=result, file_name = file_name, mime='text/plain')