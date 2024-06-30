import cv2
import numpy as np
import streamlit as st
from detections.process import process_image, annotate_image
from PIL import Image

def main():
    st.title("Object Detection for Image")
    file = st.file_uploader("Upload Image", type = ["jpg", "png", "jpeg"])
    if file is not None:
        st.image(file, caption = "Uploaded Image")

        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        processed_image = annotate_image(image, detections)
        st.image(processed_image, caption = "Processed Image")

if __name__ == "__main__":
    main()