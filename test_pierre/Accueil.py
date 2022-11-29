#===============================================================================

import matplotlib.pyplot as plt
import streamlit as st
import mediapipe as mp
import pandas as pd
from PIL import Image
import numpy as np
import random
import os
import cv2
from PIL import Image
import include

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

def main1():
    picture1 = take_a_picture()
    button1 = st.button("Convert")
    if button1:
        df1 = picture_to_df(picture1)
        st.write(df1)

def main2():
    picture2 = take_a_picture()
    button2 = st.button("Classify")
    chifoudict = {0: "pierre", 1: "feuille", 2: "ciseaux"}
    num_res = picture_to_target(picture2)
    str_res = chifoudict[num_res]
    if button2:
        st.write(f"Position de votre main : {str_res}")


def main3():
    #---------------------------------------------------------------------------
    image_path = IMAGE_PATH + "chifoumi.jpg"
    chifoumi_image = Image.open(image_path)
    #---------------------------------------------------------------------------
    col1, col2 = st.columns(2)
    #---------------------------------------------------------------------------
    #-- Colonne 1
    picture = col1.image(chifoumi_image, width=400)
    #---------------------------------------------------------------------------
    #-- Colonne 2
    picture = col2.camera_input(label=" ", disabled=False, key=2)

def main4():
    image_path = IMAGE_PATH + "chifoumi.jpg"
    chifoumi_image = Image.open(image_path)
    picture = st.image(chifoumi_image, width=600)
    #button_play = st.button("Jouer")

def main5():
    st.balloons()

main4()
