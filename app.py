# Core Pkgs
import streamlit as st
import numpy as np
import os
import time
timestr = time.strftime("%Y%M%D-%H%M")


# For QR Code
import qrcode

qr = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=14,
    )

from PIL import Image
# Function to Load Image
def load_image(img):
    im = Image.open(img)
    return im


# Application
def main():
    menu = ["Home", "DecodeQR", "About"]

    choice = st.sidebar.selectbox("เลือกรายการ",menu)

    if choice == "Home":
        st.subheader("Home")
        # Text Input

    elif choice == "DecodeQR":
        st.subheader("Decode QR")
        with st.form(key='myqr_form'):
            raw_text = st.text_area("กรอกข้อมูล")
            submit_button = st.form_submit_button("สร้าง QR Code")

        # Layout
        if submit_button:
            col1, col2 = st.columns(2)

            with col1:
                # Add Date
                qr.add_data(raw_text)
                # Generate
                qr.make(fit=True)
                img = qr.make_image(fill_color='black',back_color='white')

                #fillname
                img_filename = 'qr_img{}.png'.format(timestr)
                path_for_images = os.path.join('qr_img', img_filename)
                img.save(path_for_images)

            with col2:
                st.info("ข้อมูลต้นฉบับ")
                st.write(raw_text)


    else:
        st.subheader("About")

if __name__ == '__main__':
    main()