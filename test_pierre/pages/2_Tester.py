#===============================================================================

import streamlit as st
#from PIL import Image
from include import take_a_picture, picture_to_df, picture_to_target
import pandas as pd

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

html_title = "<h2 style='color:red'>Testons l'acquisition photo !</h2>"
st.markdown(html_title, unsafe_allow_html=True)

picture = take_a_picture(key=6453)
button1 = st.button("Test", key=1)

if button1:
    df = picture_to_df(picture)
    # st.write(type(df))
    if type(df) == type("toto"):
        st.write("Problème dans l'acquisition photo.")
    else:
        st.write(df)
        target = picture_to_target(picture)
        chifoudict = {0: "pierre", 1: "feuille", 2: "ciseaux"}
        gesture = chifoudict[target]
        st.write(f"Votre geste : {gesture}")
