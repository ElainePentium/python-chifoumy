#===============================================================================

import random
import streamlit as st
from PIL import Image
from chifoumy.interface.detection import take_a_picture, picture_to_df
from chifoumy.ml_logic.registry import load_pipeline
from chifoumy.interface.utils import create_key

#===============================================================================

IMAGE_PATH = "../images/"

#image_path = IMAGE_PATH + "logo_rock.png"
#chifoumi_image = Image.open(image_path)
#picture = st.image(chifoumi_image, width=600)
#picture = st.image(chifoumi_image, width=200)

#===============================================================================

MAX_SCORE = 3

def scoring(machine_gesture, user_gesture):
    """
    0: pierre
    1: feuille
    2: ciseaux
    """
    if user_gesture==machine_gesture:
        return "null"
    elif user_gesture==0 and machine_gesture==2:
        return "user"
    elif user_gesture == 1 and machine_gesture == 0:
        return "user"
    elif user_gesture == 2 and machine_gesture == 1:
        return "user"
    else:
        return "machine"

def scoring_spock(machine_gesture, user_gesture):
    """
    0: pierre,
    1: feuille,
    2: ciseaux
    3: python
    4: spock
    """
    if user_gesture==machine_gesture:
        return "null"
    elif user_gesture==0 and machine_gesture==2:
        return "user"
    elif user_gesture==0 and machine_gesture==3:
        return "user"
    elif user_gesture==0 and machine_gesture==1:
        return "machine"
    elif user_gesture==0 and machine_gesture==4:
        return "machine"
    elif user_gesture==1 and machine_gesture==0:
        return "user"
    elif user_gesture==1 and machine_gesture==4:
        return "user"
    elif user_gesture==1 and machine_gesture==2:
        return "machine"
    elif user_gesture==1 and machine_gesture==3:
        return "machine"
    elif user_gesture==2 and machine_gesture==1:
        return "user"
    elif user_gesture==2 and machine_gesture==3:
        return "user"
    elif user_gesture==2 and machine_gesture==4:
        return "machine"
    elif user_gesture==2 and machine_gesture==0:
        return "machine"
    elif user_gesture==3 and machine_gesture==1:
        return "user"
    elif user_gesture==3 and machine_gesture==4:
        return "user"
    elif user_gesture==3 and machine_gesture==2:
        return "machine"
    elif user_gesture==3 and machine_gesture==0:
        return "machine"
    elif user_gesture==4 and machine_gesture==0:
        return "user"
    elif user_gesture==4 and machine_gesture==2:
        return "user"
    elif user_gesture==4 and machine_gesture==1:
        return "machine"
    elif user_gesture==4 and machine_gesture==3:
        return "machine"

def description(machine_gesture, user_gesture):
    """
    0: pierre,
    1: feuille,
    2: ciseaux,
    3: python,
    4: spoke
    """

    if user_gesture == machine_gesture:
        html_description = "style='text-align:center;color:#fffa03;font-size:30px'> Match nul !"
        return html_description
    elif user_gesture == 0 and machine_gesture == 2:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'>Gagné ! PIERRE écrase CISEAUX</div>"
        return html_description
    elif user_gesture == 0 and machine_gesture == 3:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'> Gagné ! PIERRE assomme PYTHON</div>"
        return html_description
    elif user_gesture == 0 and machine_gesture == 1:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! FEUILLE recouvre PIERRE</div>"
        return html_description
    elif user_gesture == 0 and machine_gesture == 4:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! SPOKE vaporise PIERRE</div>"
        return html_description
    elif user_gesture == 1 and machine_gesture == 0:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'> Gagné ! FEUILLE recouvre PIERRE</div>"
        return html_description
    elif user_gesture == 1 and machine_gesture == 4:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'> Gagné ! FEUILLE réfute SPOKE</div>"
        return html_description
    elif user_gesture == 1 and machine_gesture == 2:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! CISEAUX découpent FEUILLE</div>"
        return html_description
    elif user_gesture == 1 and machine_gesture == 3:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! PYTHON mange FEUILLE</div>"
        return html_description
    elif user_gesture == 2 and machine_gesture == 1:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'> Gagné ! CISEAUX découpent FEUILLE</div>"
        return html_description
    elif user_gesture == 2 and machine_gesture == 3:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'> Gagné ! CISEAUX décapitent PYTHON</div>"
        return html_description
    elif user_gesture == 2 and machine_gesture == 4:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! SPOKE casse CISEAUX</div>"
        return html_description
    elif user_gesture == 2 and machine_gesture == 0:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! PIERRE écrase CISEAUX</div>"
        return html_description
    elif user_gesture == 3 and machine_gesture == 1:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'> Gagné ! PYTHON mange FEUILLE</div>"
        return html_description
    elif user_gesture == 3 and machine_gesture == 4:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'> Gagné ! PYTHON empoisonne SPOKE</div>"
        return html_description
    elif user_gesture == 3 and machine_gesture == 2:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! CISEAUX décapitent PYTHON</div>"
        return html_description
    elif user_gesture == 3 and machine_gesture == 0:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! PIERRE assomme PYTHON</div>"
        return html_description
    elif user_gesture == 4 and machine_gesture == 0:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'> Gagné ! SPOKE vaporise PIERRE</div>"
        return html_description
    elif user_gesture == 4 and machine_gesture == 2:
        html_description = "style='text-align:center;color:#6aff03;font-size:30px'> Gagné ! SPOKE casse CISEAUX</div>"
        return html_description
    elif user_gesture == 4 and machine_gesture == 1:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! FEUILLE réfute SPOKE</div>"
        return html_description
    elif user_gesture == 4 and machine_gesture == 3:
        html_description = "style='text-align:center;color:#ff1a03;font-size:30px'> Perdu ! PYTHON empoisonne SPOKE</div>"
        return html_description

#===============================================================================

html_title = "<h1 style='color:#FF036A'>Jouons contre la machine !</h1>"
st.markdown(html_title, unsafe_allow_html=True)

#-------------------------------------------------------------------------------

file = open("scores.txt", "r")
for line in file:
    tab = line.split(",")
    user_score = int(tab[0])
    machine_score = int(tab[1])
file.close()

picture = None
placeholder1 = st.empty()
picture = placeholder1.camera_input("", key=666)
if picture:
    df = picture_to_df(picture)
    # st.write(type(df))
    if type(df) == type("toto"):
        st.write("Problème dans l'acquisition photo.")
    else:
        #st.write(df)
        my_pipeline = load_pipeline(spock=True)
        target = my_pipeline.predict(df)
        target = target[0]
        #st.write(type(target))
        #st.write(target.shape)
        #html_user_pierre ="<div style='color:#E37B01;font-size:30px'>Votre geste : pierre</div>"
        #html_user_feuille ="<div style='color:#AEC90E;font-size:30px'>Votre geste : feuille</div>"
        #html_user_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Votre geste : ciseaux</div>"
        #----
        #chemin = IMAGE_PATH + "logo_rock.png"
        #st.write(chemin)
        #st.image(chemin)
        #----
        #user_dict = {0: html_user_pierre, 1: html_user_feuille, 2: html_user_ciseaux}
        #user_gesture = user_dict[target]
        #st.markdown(user_gesture, unsafe_allow_html=True)
        #----------------
        machine_play = random.randint(0, 4)
        #html_machine_pierre ="<div style='color:#E37B01;font-size:30px'>Geste machine : pierre</div>"
        #html_machine_feuille ="<div style='color:#AEC90E;font-size:30px'>Geste machine : feuille</div>"
        #html_machine_ciseaux ="<div style='color:#8B4C89;font-size:30px'>Geste machine : ciseaux</div>"
        #machine_dict = {0: html_machine_pierre, 1: html_machine_feuille, 2: html_machine_ciseaux}
        #machine_gesture = machine_dict[machine_play]
        #st.markdown(machine_gesture, unsafe_allow_html=True)
        #----------------
        # scoring
        result = scoring_spock(machine_play, target)
        if result=="machine":
            machine_score += 1
            #st.write(f"La machine vient de gagner la manche n° {game_counter}.")
        elif result=="user":
            user_score += 1
            #st.write(f"L'humain vient de gagner la manche n° {game_counter}.")
        elif result=="null":
            pass
            #st.write("Manche nulle entre l'humain et la machine.")
        user_html = f"<div style='color:#44B7E3;font-size:30px'>🙂 Score du joueur : {user_score}</div>"
        #st.markdown(user_html, unsafe_allow_html=True)
        machine_html = f"<div style='color:#44B7E3;font-size:30px'>🤖 Score de la machine : {machine_score}</div>"
        #st.markdown(machine_html, unsafe_allow_html=True)
        #st.write(f"🙂 Score du joueur : {user_score}")
        #st.write(f"🤖 Score de la machine : {machine_score}")
        file = open("scores.txt", "w")
        file.write(f"{user_score},{machine_score}")
        file.close()
        #st.write(f"✅ Les scores {machine_score} et {user_score} ont été sauvegardés.")
        #-------------------------------------------------------------------
        # Affichage amélioré
        IMAGE_PIERRE_PATH = "https://www.bejian.fr/chifoumy/images/"
        machine_image_dict = {0: "logo_rock_machine.png",1: "logo_paper_machine.png",
                            2: "logo_scissors_machine.png",3: "logo_python_machine.png",
                            4: "logo_spock_machine.png"}
        human_image_dict = {0: "logo_rock_human.png",1: "logo_paper_human.png",
                            2: "logo_scissors_human.png", 3: "logo_python_human.png",
                            4: "logo_spock_human.png"}
        image_user = IMAGE_PIERRE_PATH + human_image_dict[target]
        image_machine = IMAGE_PIERRE_PATH + machine_image_dict[machine_play]
        html_description = description(machine_play, target)
        #st.write(image_user)
        #st.write(image_machine)
        #st.image(image_machine)
        #-------
        #ai_image_path = IMAGE_PIERRE_PATH + "ai.gif"
        #ai_html = f"""
        #<div style="display:flex;justify-content:center;align-items:center;width:100%;height:100%">
        #<img src='{ai_image_path}' width='300'>
        #</div>
        #"""
        #placeholder = st.empty()
        #placeholder = st.markdown(ai_html, unsafe_allow_html=True)
        #-------
        big_html = f"""
        <div style="display:flex;justify-content:center;align-items:center;width:100%;height:100%">
        <table>
        <tr>
            <th style='text-align:center;font-size:30px'>🙂 Humain</th>
            <th style='text-align:center;font-size:30px'>🤖 Machine</th>
        </tr>
        <tr>
            <td><img src='{image_user}' width='300'></td>
            <td><img src='{image_machine}' width='300'></td>
        </tr>
        <tr>
            <td style='text-align:center;font-size:50px;color:#44B7E3'>{user_score}</td>
            <td style='text-align:center;font-size:50px;color:#44B7E3'>{machine_score} </td>
        </tr>
        <tr>
            <td colspan='2' {html_description} </td>
        </tr>
        </table>
        </div>
        <br>
        """
        st.markdown(big_html, unsafe_allow_html=True)
        #-------------------------------------------------------------------
        if machine_score==MAX_SCORE:
            final_html = f"<div style='color:#FF036A;font-size:30px'>➡️ Victoire de la machine !</div>"
            st.markdown(final_html, unsafe_allow_html=True)
        if user_score==MAX_SCORE:
            final_html = f"<div style='color:#FF036A;font-size:30px'>➡️ Victoire de l'humain !</div>"
            st.markdown(final_html, unsafe_allow_html=True)
