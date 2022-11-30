import os
import pandas as pd
from colorama import Fore, Style
from chifoumy.ml_logic.params import LOCAL_DATA_PATH

import os
import cv2
import mediapipe as mp
import pandas as pd

def from_png_to_df(hand: str, verbose=True, save=True) -> pd.DataFrame:
    """
    return a dataframe of the coordinate, from png dataset, from local disk
    if save=True, save the df in a csv file
    """
    path = os.path.join(os.path.expanduser(LOCAL_DATA_PATH),hand)
    hand_image_files = []

    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            hand_image_files.append(f)

    if verbose:
        print(Fore.MAGENTA + f"Source data from {path}" + Style.RESET_ALL)

    mp_hands = mp.solutions.hands
    hands_list = []

    with mp_hands.Hands(static_image_mode=True,
                        max_num_hands=2,
                        min_detection_confidence=0.5) as hands:
        for idx, file in enumerate(hand_image_files):

            # image = cv2.flip(cv2.imread(file), 1)
            image = cv2.imread(file)
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            if not results.multi_hand_landmarks:
                continue

            for hand_landmarks in results.multi_hand_landmarks:
                fingers = {}
                for i, finger in enumerate(hand_landmarks.landmark, start=1):
                    fingers[f'{i}x'] = (finger.x)
                    fingers[f'{i}y'] = (finger.y)
                hands_list.append(fingers)
    hand_df = pd.DataFrame(hands_list)
    hand_df['target'] = 0
    hand_df.shape

    # if save:
    #     hand_df.to_csv(os.path.join(LOCAL_DATA_PATH,{hand},'_df.csv'), index=False)

    return hand_df


def save_data(data: pd.DataFrame, is_first: bool):
    """
    save the dataset to local disk
    """

    path = os.path.join(os.path.expanduser(LOCAL_DATA_PATH))

    print(Fore.BLUE + f"\nSave data to {path}:" + Style.RESET_ALL)

    data.to_csv(path,
                mode="w" if is_first else "a",
                header=is_first,
                index=False)

    data.to_csv(os.path.join(LOCAL_DATA_PATH,{hand},'_df.csv'), index=False)
