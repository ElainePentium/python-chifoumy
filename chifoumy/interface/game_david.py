import random
from detection import take_a_picture, picture_to_df, picture_to_target
import streamlit as st


user_score = 0
machine_score = 0
nuls = 0

placeholder = st.empty()
button2 = placeholder.button('Stopper le jeu')

user_name = input("Veuillez saisir votre nom :")

while user_score < 10 or machine_score < 10:
    st.write(f"Score de {user_name} : {user_score}")
    st.write(f"Score de la machine : {machine_score}")

    picture = None
    picture = take_a_picture(key=6453)

    if picture:
        button1 = st.button("Faites votre signe", key=1)

    if button1:
        df = picture_to_df(picture)
        if type(df) == type("toto"):
            st.write("Problème dans l'acquisition photo.")
        else:
            result = picture_to_target(picture)
    if result[0] == 0:
        player_sign = 'p'
    elif result[0] == 1:
        player_sign = 'f'
    elif result[0] == 2:
        player_sign = 'c'
    if button2:
        st.write("Vous quittez le jeu, merci d'avoir joué")
        break
    if not button2:
        # signe du joueur
        if player_sign != 'p' and player_sign != 'f' and player_sign != 'c':
            continue
        if player_sign == 'p':
            st.write("PIERRE contre ...", end = ' ')
        elif player_sign == 'f':
            st.write("FEUILLE contre ...", end = ' ')
        else:
            st.write("CISEAUX contre ...", end = ' ')

        # signe de la machine
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

        # comparaisons des signes joués et incrémentation des scores
        if player_sign == machine_sign:
            st.write('Match nul!')
            nuls += 1
        elif player_sign == 'p' and machine_sign == 'c':
            user_count += 1
            st.write("You win!")
        elif player_sign == 'f' and machine_sign == 'p':
            user_count =+ 1
            st.write("You win!")
        elif player_sign == 'c' and machine_sign == 'f':
            user_count =+ 1
            st.write("You win!")
        else:
            machine_count =+ 1
            st.write("You loose! The IA wins")
