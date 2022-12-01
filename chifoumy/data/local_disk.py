import os
import pandas as pd
from colorama import Fore, Style
from chifoumy.ml_logic.params import LOCAL_DATA_PATH

import os
import cv2
import mediapipe as mp
import pandas as pd

def from_png_to_csv(hand: str, verbose=True):
    """
    return a dataframe with the coordinate of one gesture, from png files,
    stored in a directory with the name of the gesture, from local disk.

    hand: str > shape/gesture (rock, paper, scissors)
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
                        max_num_hands=1,
                        min_detection_confidence=0.5) as hands:

        for idx, file in enumerate(hand_image_files):

            image_vanilla = cv2.imread(file)
            image_flip = cv2.flip(cv2.imread(file), 1)
            image_up = cv2.rotate(cv2.imread(file), cv2.ROTATE_90_COUNTERCLOCKWISE)
            image_down = cv2.rotate(cv2.imread(file), cv2.ROTATE_90_CLOCKWISE)

            results_vanilla = hands.process(cv2.cvtColor(image_vanilla, cv2.COLOR_BGR2RGB))
            results_flip = hands.process(cv2.cvtColor(image_flip, cv2.COLOR_BGR2RGB))
            results_up = hands.process(cv2.cvtColor(image_up, cv2.COLOR_BGR2RGB))
            results_down = hands.process(cv2.cvtColor(image_down, cv2.COLOR_BGR2RGB))

            if not results_vanilla.multi_hand_landmarks or not results_flip.multi_hand_landmarks \
               or not results_up.multi_hand_landmarks or not results_down.multi_hand_landmarks:
                if verbose:
                   print(Fore.YELLOW + f"{idx} {file}: no multi_hand_landmarks found" + Style.RESET_ALL)

                continue

            # if verbose:
            #        print(Fore.BLUE + f"hand {idx} landmarking" + Style.RESET_ALL)

            for hand_landmarks in results_vanilla.multi_hand_landmarks:

                fingers = {
                    'filename' : file
                }

                for i, finger in enumerate(hand_landmarks.landmark, start=1):
                    fingers[f'{i}x'] = (finger.x)
                    fingers[f'{i}y'] = (finger.y)
                    fingers[f'{i}z'] = (finger.z)

                hands_list.append(fingers)

            for hand_landmarks in results_flip.multi_hand_landmarks:

                fingers = {
                    'filename' : file
                }

                for i, finger in enumerate(hand_landmarks.landmark, start=1):
                    fingers[f'{i}x'] = (finger.x)
                    fingers[f'{i}y'] = (finger.y)
                    fingers[f'{i}z'] = (finger.z)


                hands_list.append(fingers)

            for hand_landmarks in results_up.multi_hand_landmarks:

                fingers = {
                    'filename' : file
                }

                for i, finger in enumerate(hand_landmarks.landmark, start=1):
                    fingers[f'{i}x'] = (finger.x)
                    fingers[f'{i}y'] = (finger.y)
                    fingers[f'{i}z'] = (finger.z)

                hands_list.append(fingers)

            for hand_landmarks in results_down.multi_hand_landmarks:

                fingers = {
                    'filename' : file
                }

                for i, finger in enumerate(hand_landmarks.landmark, start=1):
                    fingers[f'{i}x'] = (finger.x)
                    fingers[f'{i}y'] = (finger.y)
                    fingers[f'{i}z'] = (finger.z)

                hands_list.append(fingers)


    hand_df = pd.DataFrame(hands_list)
    hand_df['target'] = 0

    # if save:
    #     hand_df.to_csv(os.path.join(LOCAL_DATA_PATH,{hand},'_df.csv'), index=False)

    return hand_df


def save_data(data: pd.DataFrame, hand: str, is_first: bool):
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


df = from_png_to_csv('rock')
df.head()
