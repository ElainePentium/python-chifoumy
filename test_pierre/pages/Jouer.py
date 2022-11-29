#===============================================================================

import streamlit as st
from PIL import Image

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

def main3():
    #---------------------------------------------------------------------------
    image_path1 = IMAGE_PATH + "chifoumi.jpg"
    chifoumi_image = Image.open(image_path1)
    image_path2 = IMAGE_PATH + "blank.jpg"
    blank_image = Image.open(image_path2)

    #---------------------------------------------------------------------------
    col1, col2 = st.columns(2)
    #---------------------------------------------------------------------------
    #-- Colonne 1
    picture = col1.image(chifoumi_image, width=400)
    #-- Colonne 2
    picture = col2.camera_input(label=" ", disabled=False, key=1)

#===============================================================================

main3()
