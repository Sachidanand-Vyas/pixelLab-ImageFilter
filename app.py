import streamlit as st
import numpy as np
from PIL import Image
import cv2


st.title("PixelLab AI")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png", "webp", "tiff"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    image_array = np.array(image)
    #shape of image
    st.write("Image Shape:", image_array.shape)

    #grayscale image of the og image

    def gray_image():
        gray=cv2.cvtColor(image_array,cv2.COLOR_RGB2GRAY)
        return gray
    
    def blur_image():
        blur=cv2.GaussianBlur(image_array,(51,51),0)
        return blur

    def invert_image():
        invert=255-image_array
        return invert
    
    def brightness_filter(value=30):
        
        bright = np.clip(image_array.astype(np.int16) + value, 0, 255)

        return bright.astype(np.uint8)
    
    def contrast_filter(alpha=1.5):
        contrast = np.clip(image_array.astype(np.float32) * alpha, 0, 255)

        return contrast.astype(np.uint8)
    
    def edge_detection():
        gray=cv2.cvtColor(image_array,cv2.COLOR_RGB2GRAY)
        edges=cv2.Canny(gray,100,200)
        return edges
    
    def sharpen_filter():

        kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
        ])

        sharpen = cv2.filter2D(image_array, -1, kernel)

        return sharpen
    def sepia_filter():

        kernel = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189]
        ])

        sepia = cv2.transform(image_array, kernel)

        sepia = np.clip(sepia, 0, 255)

        return sepia.astype(np.uint8)


# 9. Black & White Threshold Filter
    def threshold_filter():

        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

        _, threshold = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
        )

        return threshold


# 10. Red Channel Filter
    def red_filter():

        red = image_array.copy()

        red[:, :, 1] = 0
        red[:, :, 2] = 0

        return red


# 11. Green Channel Filter
    def green_filter():

        green = image_array.copy()

        green[:, :, 0] = 0
        green[:, :, 2] = 0

        return green


# 12. Blue Channel Filter
    def blue_filter():

        blue = image_array.copy()

        blue[:, :, 0] = 0
        blue[:, :, 1] = 0

        return blue
    

    #st.image(gray_image(), caption="Grayscale filter")
    #st.image(invert_image(),caption="invert filter")
    #st.image(blur_image(),caption="blur filter")
    #st.image(brightness_filter(),caption="brightness filter")
    #st.image(contrast_filter(),caption="contrast filter")
    #st.image(edge_detection(),caption="edge detection filter")
    #st.image(sharpen_filter(),caption="sharpen filter")
    #st.image(sepia_filter(),caption="sephia filter")
    #st.image(threshold_filter(),caption="threshold filter")
    #st.image(red_filter(),caption="red filter")
    #st.image(blue_filter(),caption="blue filter")
    #st.image(green_filter(),caption="green filter")
     
    #dropdown of selected filter]
    selected_filter=st.selectbox("choose filter",[
        "Original",
        "Grayscale",
        "Invert",
        "Blur",
        "Brightness",
        "Contrast",
        "Edge Detection",
        "Sharpen",
        "Sepia",
        "Threshold",
        "Red Filter",
        "Green Filter",
        "Blue Filter"
    ])

    if selected_filter == "Original":

        processed_image = image_array

    elif selected_filter == "Grayscale":

        processed_image = gray_image()

    elif selected_filter == "Invert":

        processed_image = invert_image()

    elif selected_filter == "Blur":

        processed_image = blur_image()

    elif selected_filter == "Brightness":

        processed_image = brightness_filter()

    elif selected_filter == "Contrast":

        processed_image = contrast_filter()

    elif selected_filter == "Edge Detection":

        processed_image = edge_detection()

    elif selected_filter == "Sharpen":

        processed_image = sharpen_filter()

    elif selected_filter == "Sepia":

        processed_image = sepia_filter()

    elif selected_filter == "Threshold":

        processed_image = threshold_filter()

    elif selected_filter == "Red Filter":

        processed_image = red_filter()

    elif selected_filter == "Green Filter":

        processed_image = green_filter()

    elif selected_filter == "Blue Filter":

        processed_image = blue_filter()

    st.image(processed_image,caption=f"{selected_filter} filter",use_container_width=True)