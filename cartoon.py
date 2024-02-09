import streamlit as st
import numpy as np
from PIL import Image, ImageFilter, ImageOps

def cartoonify_image(image, cartoon_intensity=5):
    # Convert image to numpy array
    img = np.array(image)
    
    # Convert to grayscale
    gray = ImageOps.grayscale(image)
    
    # Apply Gaussian blur
    blur = gray.filter(ImageFilter.GaussianBlur(cartoon_intensity))
    
    # Apply edge enhancement
    edge_enhanced = ImageOps.equalize(blur, mask=None)
    
    # Invert colors
    inverted = ImageOps.invert(edge_enhanced)
    
    # Convert back to RGB
    cartoon = inverted.convert('RGB')
    
    return cartoon

# Streamlit code
st.title('Cartoonify Your Image')
st.write('Upload your image and see the magic!')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    st.subheader('Original Image')
    st.image(image, use_column_width=True)
    
    cartoon_intensity = st.slider('Select the intensity of cartoonify (Higher value for more intense)', min_value=1, max_value=15, value=5)
    
    cartoon_img = cartoonify_image(image, cartoon_intensity)
    
    st.subheader('Cartoonified Image')
    st.image(cartoon_img, use_column_width=True)
