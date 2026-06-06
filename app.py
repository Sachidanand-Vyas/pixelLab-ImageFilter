import streamlit as st
import numpy as np
from PIL import Image
import cv2
from filters import *
from rembg import remove
from io import BytesIO



st.title("PixelLab")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png", "webp", "tiff"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
    except Exception as e:
        print("error loading image")

    
    image_array = np.array(image)
    #shape of image
    st.write("Image Shape:", image_array.shape)

    #grayscale image of the og image

    
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
    selected_filter=st.sidebar.selectbox("choose filter",[
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

        processed_image = gray_image(image_array)

    elif selected_filter == "Invert":

        processed_image = invert_image(image_array)

    elif selected_filter == "Blur":
        blur_value=st.sidebar.slider("Blur strength",1,101,15,step=2)

        processed_image = blur_image(image_array,blur_value)

    elif selected_filter == "Brightness":
        brightness_value=st.sidebar.slider("Brightness",-100,100,0)

        processed_image = brightness_filter(image_array,brightness_value)

    elif selected_filter == "Contrast":
        contrast_value=st.sidebar.slider("Contrast level",0.1,3.0,1.0,step=0.1)

        processed_image = contrast_filter(image_array,contrast_value)

    elif selected_filter == "Edge Detection":
        low_threshold=st.sidebar.slider("low threshold",0,255,100)
        high_threshold=st.sidebar.slider("high threshold",0,255,200)

        processed_image = edge_detection(image_array,low_threshold,high_threshold)

    elif selected_filter == "Sharpen":
        sharpness_strength=st.sidebar.slider("Sharpness Strength",0.0,2.0,0.5,step=0.1)

        processed_image = sharpen_filter(image_array,sharpness_strength)

    elif selected_filter == "Sepia":
        sepia_strength=st.sidebar.slider("sepia strength",0.0,1.0,0.5,step=0.1)

        processed_image = sepia_filter(image_array,sepia_strength)

    elif selected_filter == "Threshold":
        threshold_value=st.sidebar.slider("threshold slider",0,255,127)

        processed_image = threshold_filter(image_array,threshold_value)

    elif selected_filter == "Red Filter":
        red_intensity=st.sidebar.slider("red value",1.0,3.0,1.5,step=0.1)
        processed_image = red_filter(image_array,red_intensity)

    elif selected_filter == "Green Filter":
        green_intensity=st.sidebar.slider("green value",1.0,3.0,1.5,step=0.1)
        processed_image = green_filter(image_array,green_intensity)

        

    elif selected_filter == "Blue Filter":
        blue_intensity=st.sidebar.slider("blue value",1.0,3.0,1.5,step=0.1)

        processed_image = blue_filter(image_array,blue_intensity)
    remove_bg = st.sidebar.checkbox("Remove Background")

    if remove_bg:
        with st.spinner("Removing background..."):
            processed_image = remove(processed_image)
    col1, col2 = st.columns(2)

    with col1:
        st.image(
            image_array,
            caption="Original Image",
            use_container_width=True
        )

    with col2:
        st.image(
            processed_image,
            caption=f"{selected_filter} Filter",
            use_container_width=True
        )     

        

    download_format = st.sidebar.selectbox(
    "Download Format",
    ["PNG", "JPG", "WEBP"]
)

# Handle rembg output
    if isinstance(processed_image, bytes):
        result_image = Image.open(BytesIO(processed_image))
    else:
        result_image = Image.fromarray(processed_image)

# JPG doesn't support transparency
    if download_format == "JPG":
        if result_image.mode == "RGBA":
            result_image = result_image.convert("RGB")

    buffer = BytesIO()

    save_format = download_format

    if save_format == "JPG":
        save_format = "JPEG"

    result_image.save(
        buffer,
        format=save_format
    )

    mime_types = {
        "PNG": "image/png",
        "JPG": "image/jpeg",
     "WEBP": "image/webp"
    }

    st.download_button(
        label=f"Download {download_format}",
        data=buffer.getvalue(),
        file_name=f"filtered_image.{download_format.lower()}",
        mime=mime_types[download_format]
    )
    
    theme=st.sidebar.selectbox("Theme",["Dark","Light","Ocean","Purple"])
    if theme == "Dark":

        st.markdown(
            """
            <style>
            .stApp {
                background-color: #0E1117;
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    elif theme == "Light":

        st.markdown(
            """
            <style>
            .stApp {
                background-color: white;
                color: black;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    elif theme == "Ocean":

        st.markdown(
            """
            <style>
            .stApp {
                background-color: #0F2027;
                color: #A8DADC;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    elif theme == "Purple":

        st.markdown(
            """
            <style>
            .stApp {
                background-color: #2D1E2F;
                color: #E0AAFF;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    
   