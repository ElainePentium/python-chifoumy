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
import pickle
import time

#===============================================================================


def take_a_picture(key=1):
    """
    Do not forget to change the key for multiple camera
    """
    picture = st.camera_input(label=" ", disabled=False, key=key)
    return picture


def picture_to_df(picture):
    """
    Docstring
    """
    hand_list = []
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
        # Read the image, flip it around y-axis for correct handedness output (see above)
        # image = cv2.flip(cv2.imread(picture), 1)
        img = Image.open(picture)
        img_array = np.array(img)
        # image = cv2.flip(img_array, 1)
        image = img_array
        # st.image(image)
        #-------------------------------------
        # Convert the BGR image to RGB before processing.
        # results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        results = hands.process(image)
        if not results.multi_hand_landmarks:
            return "No hand in this picture!"
        # annotated_image = image.copy()
        for hand_landmarks in results.multi_hand_landmarks:
            # print((hand_landmarks.landmark))
            fingers = {}
            for i, finger in enumerate(hand_landmarks.landmark, start=1):
                fingers[f'{i}x'] = (finger.x)
                fingers[f'{i}y'] = (finger.y)
                fingers[f'{i}z'] = (finger.z)
            hand_list.append(fingers)
        return  pd.DataFrame(hand_list)



def create_key():
    t = time.perf_counter_ns()
    return t
