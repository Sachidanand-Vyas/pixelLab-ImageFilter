import streamlit as st
from PIL import Image

st.title("PixelLab AI")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png","webp","tiff"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")