# Core Pkgs
import streamlit as st
import numpy as np


# Application
def main():
    menu = ["Home", "DecodeQR", "About"]

    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        


if __name__ == '__main__':
    main()