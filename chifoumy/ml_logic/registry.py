import os
import time
import pickle
import glob
from colorama import Fore, Style
from chifoumy.ml_logic.params import LOCAL_REGISTRY_PATH


def save_pipeline(pipeline = None, metrics = None):
    """
    save pipeline
    """
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    print(Fore.BLUE + "\nSave model to local disk..." + Style.RESET_ALL)

    if pipeline is not None:
        pipe_path = os.path.join(LOCAL_REGISTRY_PATH, "model_pipe" + timestamp + ".pickle")

        with open(pipe_path, "wb") as file:
            pickle.dump(pipeline, file)

        print("\n💾 pipeline saved")

    if metrics is not None:
        metrics_path = os.path.join(LOCAL_REGISTRY_PATH, "metrics" + timestamp + ".pickle")
        with open(metrics_path, "wb") as file:
            pickle.dump(metrics, file)

    return None


def load_pipeline() -> object:
    """
    load the latest saved model, return None if no model found
    """
    print(Fore.BLUE + "\n⏳ Load pipeline from local disk..." + Style.RESET_ALL)

    # get latest model_pipeline version
    pipe_directory = os.path.join(LOCAL_REGISTRY_PATH)

    results = glob.glob(f"{pipe_directory}/*")
    if not results:
        return None

    pipe_path = sorted(results)[-1]
    # print(f"- path: {pipe_path}")

    pipeline = pickle.load(open(pipe_path, "rb"))
    print("\n✅ model loaded from disk")

    return pipeline


def save_model(model = None, metrics = None):
    """
    save model
    """
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    print(Fore.BLUE + "\nSave model to local disk..." + Style.RESET_ALL)

    if model is not None:
        model_path = os.path.join(LOCAL_REGISTRY_PATH, "model" + timestamp + ".pickle")

        with open(model_path, "wb") as file:
            pickle.dump(model, file)

        print("\n💾 model saved")

    if metrics is not None:
        metrics_path = os.path.join(LOCAL_REGISTRY_PATH, "metrics" + timestamp + ".pickle")
        with open(metrics_path, "wb") as file:
            pickle.dump(metrics, file)

    return None
