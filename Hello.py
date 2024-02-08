import streamlit as st
st.set_page_config(page_title='cartoonify')        
st.title("Cartoon effect on image")   

uploaded_file = st.file_uploader("Choose an image...", type=["png"])

if uploaded_file is not None:
    # Display the image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
