from chifoumy.ml_logic.params import LOCAL_REGISTRY_PATH

import os
import pickle

from colorama import Fore, Style

def save_pipeline(pipeline = None):
    """
    save pipeline
    """
    print(Fore.BLUE + "\nSave model to local disk..." + Style.RESET_ALL)

    if pipeline is not None:
        pipeline_path = os.path.join(LOCAL_REGISTRY_PATH, "pipeline.pkl")
        print(f"- pipeline path: {pipeline_path}")

        with open(pipeline_path, "wb") as file:
            pickle.dump(pipeline, file)

        print("\n✅ data saved locally")

    return None


def load_pipeline() -> object:
    """
    load the latest saved model, return None if no model found
    """
    print(Fore.BLUE + "\nLoad model from local disk..." + Style.RESET_ALL)

    pipeline_path = os.path.join(LOCAL_REGISTRY_PATH, "pipeline.pkl")
    print(f"- pipeline path: {pipeline_path}")

    pipeline = pickle.load(open(pipeline_path, "rb"))
    print("\n✅ model loaded from disk")

    return pipeline
