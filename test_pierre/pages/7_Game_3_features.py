import random
from detection import take_a_picture, picture_to_df, picture_to_target
from chifoumy.interface.detection import load_pipeline
import streamlit as st


user_score = 0
machine_score = 0
nuls = 0

# signe du joueur
def player_play(picture):

    df = picture_to_df(picture)
    pipeline = load_pipeline()
    result = pipeline.predict(df)

    if result[0] == 0:
        player_sign = 'p'
    elif result[0] == 1:
        player_sign = 'f'
    elif result[0] == 2:
        player_sign = 'c'

    return player_sign

# signe de la machine
def machine_play():

    randomNb = random.randint(0,2)
    if randomNb == 0:
        machine_sign = 'p'
        st.write('PIERRE')
    elif randomNb == 1:
        machine_sign = 'f'
        st.write('FEUILLE')
    else:
        machine_sign = 'c'
        st.write('CISEAUX')

    return machine_sign

# comparaisons des signes joués et incrémentation des scores
def scoring(machine_sign, player_sign):
    global user_score, machine_score, nuls
    if player_sign == machine_sign:
        st.write('Match nul!')
        nuls += 1
    elif player_sign == 'p' and machine_sign == 'c':
        user_score += 1
        st.write("You win!")
    elif player_sign == 'f' and machine_sign == 'p':
        user_score =+ 1
        st.write("You win!")
    elif player_sign == 'c' and machine_sign == 'f':
        user_score =+ 1
        st.write("You win!")
    else:
        machine_score =+ 1
        st.write("You loose! The IA wins")


# structure du flow jouer

# variables globales
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
                player_sign = player_play(picture)
                machine_sign = machine_play()

                if player_sign != 'p' and player_sign != 'f' and player_sign != 'c':
                    st.write ("Signe non reconnu, veuillez recommencer.")
                    continue

                if player_sign == 'p':
                    st.write("PIERRE contre ...", end = ' ')
                elif player_sign == 'f':
                    st.write("FEUILLE contre ...", end = ' ')
                elif player_sign == 'c':
                    st.write("CISEAUX contre ...", end = ' ')

                scoring(player_sign, machine_sign)
