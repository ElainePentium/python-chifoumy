#===============================================================================

import streamlit as st
from PIL import Image
from include import take_a_picture

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================



html_title = "<h2 style='color:red'>Jouons contre la machine !</h2>"
st.markdown(html_title, unsafe_allow_html=True)

jeu_en_cours = 1

#while jeu_en_cours:
#    picture = take_a_picture(key=6453)
#    button1 = st.button("Test", key=1)



def main3():
    #---------------------------------------------------------------------------
    image_path1 = IMAGE_PATH + "ai.png"
    chifoumi_image = Image.open(image_path1)
    image_path2 = IMAGE_PATH + "blank.jpg"
    blank_image = Image.open(image_path2)
    # picture = st.camera_input(label="", disabled=False, key=17645)




#===============================================================================

main3()
