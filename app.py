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
    border=14)

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
        image_file = st.file_uploader("ส่งภาพ",type=['jpg','png','jpeg'])

        if image_file is not None:
            img = load_image(image_file)
            st.image(img)
        # Text Input
        st.caption("Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia voluptas tempora molestiae possimus laboriosam consequuntur voluptate ipsam eligendi quidem itaque accusantium ullam magni, odit eos magnam similique sint quaerat distinctio. Commodi non quae tenetur, explicabo cum libero doloribus asperiores? Quo ipsa quia illo maxime ipsum laboriosam voluptates omnis facere")

    elif choice == "DecodeQR":
        st.subheader("สร้าง QR Code")
        with st.form(key='myqr_form'):
            raw_text = st.text_area("กรอกข้อมูล..ที่นี่")
            submit_button = st.form_submit_button("คลิกสร้าง QR Code")

        # Layout
        if submit_button:
            col1, col2 = st.columns(2)

            with col1:
                # Add Date
                qr.add_data(raw_text)
                # Generate
                qr.make(fit=True)
                img = qr.make_image(fill_color='black',back_color='white')

                # fillname
                img_filename = 'image_folder{}.png'.format(timestr)
                img_folder = os.path.join('image_folder', img_filename)
                img.save(img_folder)

                final_img = load_image(img_folder)
                st.image(final_img)

            with col2:
                st.info("ข้อมูลต้นฉบับ")
                st.write(raw_text)

    else:
        st.subheader("About")
        st.caption("Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia voluptas tempora molestiae possimus laboriosam consequuntur voluptate ipsam eligendi quidem itaque accusantium ullam magni, odit eos magnam similique sint quaerat distinctio. Commodi non quae tenetur, explicabo cum libero doloribus asperiores? Quo ipsa quia illo maxime ipsum laboriosam voluptates omnis facere")
        # st.image("https://drive.google.com/file/d/1ozvb8unPKquo80q_bTm3XWCt9QF4iOwj/view?usp=drive_link")
        # img = load_image("https://drive.google.com/file/d/1ozvb8unPKquo80q_bTm3XWCt9QF4iOwj/view?usp=drive_link")
        st.image(img)
        

if __name__ == '__main__':
    main()