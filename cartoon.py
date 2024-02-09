import streamlit as st
from PIL import Image, ImageFilter

def cartoonify_image(image, cartoon_intensity=5):
    # Apply Gaussian blur
    blur = image.filter(ImageFilter.GaussianBlur(cartoon_intensity))
    
    return blur

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
