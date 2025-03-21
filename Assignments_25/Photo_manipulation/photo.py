import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import io

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def apply_blur(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius))

def main():
    st.title("🖼️ Photo Manipulation App")
    st.write("Upload an image to adjust its brightness, contrast, and apply blur effects.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption='Original Image', use_container_width=True)

        st.sidebar.header("Adjustments")
        brightness = st.sidebar.slider("Brightness", 0.1, 3.0, 1.0)
        contrast = st.sidebar.slider("Contrast", 0.1, 3.0, 1.0)
        blur_radius = st.sidebar.slider("Blur", 0.0, 10.0, 0.0)

        adjusted_image = adjust_brightness(image, brightness)
        adjusted_image = adjust_contrast(adjusted_image, contrast)
        adjusted_image = apply_blur(adjusted_image, blur_radius)

        st.image(adjusted_image, caption='Adjusted Image', use_container_width=True)

        buf = io.BytesIO()
        adjusted_image.save(buf, format='PNG')
        byte_im = buf.getvalue()
        st.download_button(
            label="Download Adjusted Image",
            data=byte_im,
            file_name="adjusted_image.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
