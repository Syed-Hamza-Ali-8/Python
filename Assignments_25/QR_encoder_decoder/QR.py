import streamlit as st
import qrcode
import cv2
import numpy as np
from PIL import Image

st.title("📱 QR Code Encoder / Decoder")

option = st.selectbox("Choose Option:", ["Encode QR Code", "Decode QR Code"])

if option == "Encode QR Code":
    text = st.text_input("Enter text / URL:")
    if st.button("Generate QR Code"):
        qr = qrcode.make(text)
        qr.save("generated_qr.png")
        st.image("generated_qr.png")
        st.success("QR Code Generated!")

elif option == "Decode QR Code":
    uploaded_file = st.file_uploader("Upload QR Code Image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            st.success(f"Decoded Data: {data}")
        else:
            st.error("No QR Code detected!")
