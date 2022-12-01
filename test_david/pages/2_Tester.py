#===============================================================================

import streamlit as st
#from PIL import Image
from include import take_a_picture, picture_to_df, picture_to_target
import pandas as pd

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Testons l'acquisition photo !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

picture = None
picture = take_a_picture(key=6453)
if picture:
    button1 = st.button("Tester la photo", key=1)

    if button1:
        df = picture_to_df(picture)
        # st.write(type(df))
        if type(df) == type("toto"):
            st.write("Problème dans l'acquisition photo.")
        else:
            st.write(df)
            # st.write(df.shape)
            # ###### target = picture_to_target(picture)
            #st.write(type(target))
            #st.write(target)
            #result = target[0][0]
            #prob = target[1][0]

            #st.write(target[0])
            #st.write(type(target[0]))
            prob_pierre = round((target[1][0][0])*100)
            prob_feuille = round((target[1][0][1])*100)
            prob_ciseaux = round((target[1][0][2])*100)
            st.write (f'probabilité de Pierre : {prob_pierre} %')
            st.write (f'probabilité de Feuille : {prob_feuille} %')
            st.write (f'probabilité de Ciseaux : {prob_ciseaux} %')

            #st.write(type(target))
            #st.write(target.shape)
            html_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
            html_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
            html_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
            chifoudict = {0: html_pierre, 1: html_feuille, 2: html_ciseaux}
            html_gesture = chifoudict[target[0][0]]
            st.markdown(html_gesture, unsafe_allow_html=True)
