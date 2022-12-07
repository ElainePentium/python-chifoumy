#===============================================================================

import streamlit as st
from PIL import Image
from include import take_a_picture
from chifoumy.interface.game_5_features import player_play, machine_play, scoring
from chifoumy.interface.detection import picture_to_df

#===============================================================================

IMAGE_PATH = "../images/"

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Jouons contre la machine !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

#jeu_en_cours = 1

#while jeu_en_cours:
#    picture = take_a_picture(key=6453)
#    button1 = st.button("Test", key=1)


def main3():
    #---------------------------------------------------------------------------
    image_path1 = IMAGE_PATH + "ai.png"
    chifoumi_image = Image.open(image_path1)
    image_path2 = IMAGE_PATH + "blank.jpg"
    blank_image = Image.open(image_path1)
    # picture = st.camera_input(label="", disabled=False, key=17645)

#===============================================================================

# main3()

#===============================================================================

user_score = 0
machine_score = 0
nuls = 0

user_name = input("Veuillez saisir votre nom :")
WIN_SCORE = input("Score pour gagner")

while user_score < WIN_SCORE and machine_score < WIN_SCORE:
    st.write(f"Score de {user_name} : {user_score}")
    st.write(f"Score de la machine : {machine_score}")

    picture = take_a_picture(key=6453)

    if picture:
        placeholder = st.empty()
        button1 = placeholder.button("Faites jouer l'IA", key=1)
        button2 = placeholder.button('Recommencer le jeu', key=2)
        button3 = placeholder.button('Quitter le jeu', key=3)

        if button3:
            st.write("Vous quittez le jeu, merci d'avoir joué !")
            placeholder = st.empty()
            break

        if button2:
            st.write("Remise des scores à zéro ...")
            # global user_score, nuls, machine_score
            user_score = 0
            machine_score = 0
            nuls = 0
            continue

        if button1:

            #placeholder = st.empty()
            df = picture_to_df(picture)

            if type(df) == type("toto"):
                st.write("Problème dans l'acquisition photo.")
            else:
                player_sign = player_play()
                machine_sign = machine_play()

                if player_sign != 'p' and player_sign != 'f' and player_sign != 'c'\
                    and player_sign != 'py' and player_sign != 'sp':
                    st.write ("Signe non reconnu, veuillez recommencer.")
                    continue

                if player_sign == 'p':
                    st.write("PIERRE contre ...", end = ' ')
                elif player_sign == 'f':
                    st.write("FEUILLE contre ...", end = ' ')
                elif player_sign == 'c':
                    st.write("CISEAUX contre ...", end = ' ')
                elif player_sign == 'py':
                    st.write("PYTHON contre ...", end = ' ')
                else:
                    st.write("SPOKE contre ...", end = ' ')

                scoring(player_sign, machine_sign)
