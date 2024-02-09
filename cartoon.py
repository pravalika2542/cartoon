
#importing the package
import streamlit as st
import cv2
import numpy as np

#setting the pagetitle
st.set_page_config(page_title='cartoonify')   
#setting the heading of the page
st.title("Cartoon effect on image")   

#uploading an user input(img)
uploaded_file = st.file_uploader("Choose an image...", type=["png"])
#displaying the uploaded image
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    
    # Convert the file to an opencv image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    
