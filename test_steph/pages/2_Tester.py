#===============================================================================

import streamlit as st
#from PIL import Image
from include import take_a_picture, picture_to_df, picture_to_target
import pandas as pd
import numpy as np

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
            #st.write(df)
            target, pred_proba = picture_to_target(picture)
            # target = target[0] -> numpy.int64

            prob_pierre = round((pred_proba[0][0])*100)
            prob_feuille = round((pred_proba[0][1])*100)
            prob_ciseaux = round((pred_proba[0][2])*100)

            st.write(type(pred_proba))
            # pred_proba['equal_or_lower_than_4?'] = df['set_of_numbers'].apply(lambda x: 'True' if x <= 4 else 'False')
            # st.write(df)

            st.write(np.where(pred_proba < 0.834, False, True))
            # if pred_proba < 0.834:
            #     st.write('Retake picture!')

            st.write(f"{prob_pierre}, {prob_feuille}, {prob_ciseaux}")
            # st.write(pred_proba.shape)
            html_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
            html_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
            html_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
            chifoudict = {0: html_pierre, 1: html_feuille, 2: html_ciseaux}
            # html_gesture = chifoudict[pred_proba[0][0]]
            html_gesture = chifoudict[int(target[0])]
            st.markdown(html_gesture, unsafe_allow_html=True)
