import streamlit as st
import cv2
import numpy as np

def cartoonize_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply median blur
    median = cv2.medianBlur(blur, 5)
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(median, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    # Create a bilateral filter for the image
    color = cv2.bilateralFilter(image, 9, 300, 300)
    # Combine edges and color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

st.title('Cartoonizer')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the file to an opencv image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Perform cartoon effect
    cartoon_image = cartoonize_image(image)

    # Display the original and cartoonized image
    st.image([image, cartoon_image], caption=['Original Image', 'Cartoonized Image'], width=300)
