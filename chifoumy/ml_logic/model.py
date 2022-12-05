import numpy as np
import pandas as pd
import os

from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from chifoumy.ml_logic.preprocessor import preprocess_features
from chifoumy.ml_logic.registry import save_pipeline, load_pipeline
from chifoumy.ml_logic.params import LOCAL_CSV_PATH

# def split_sets (X, y, test_size):
#     return train_test_split(X, y, test_size)

def initialize_model():
    model = SVC(kernel= 'poly', gamma = 1, coef0 = 0, C = 0.01, probability=True)
    return model

def pipeline_constructor():
    pipeline = make_pipeline(preprocess_features, initialize_model)
    return pipeline

def model_in_pipeline(preprocess_pipeline):
    model = SVC(kernel= 'poly', gamma = 1, coef0 = 0, C = 0.01, probability=True)
    pipeline = make_pipeline(preprocess_pipeline, model)

    return pipeline

def preprocess_and_train():
    """
    Load data in memory, preprocess it, through a pipeline in which
    we add a SVC model, train the pipeline and save it locally
    """

    print("\n⭐️ Use case: preprocess and train basic")


    # Retrieve raw data
    data_raw_path = os.path.join(LOCAL_CSV_PATH, "chifoumi-dataset.csv")
    data = pd.read_csv(data_raw_path) #, dtype='float64')

    # data already cleaned

    # Create X, y
    X = data.drop(['filename', 'target'], axis = 1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Preprocess in a pipeline using `preprocessor.py`
    preprocess_pipeline = preprocess_features(X_train)
    print(f"\n🧪 X preprocessed in a pipeline")

    # Train model on X_processed and y, using `model.py`
    model_pipeline = model_in_pipeline(preprocess_pipeline)

    # model_pipeline = pipeline_constructor(X_train)
    model_pipeline.fit(X_train, y_train)

    print("\n💪 model entrainé et pipelinisé")

    # Save trained model
    save_pipeline(model_pipeline) #, metrics)

    # 🧪 Write outputs so that they can be tested by make test_train_at_scale (do not remove)
    # write_result(name="test_preprocess_and_train", subdir="train_at_scale", metrics=metrics)

    print("\n✅ preprocess_and_train() done")

    return X_test, y_test


def pred(X_pred: pd.DataFrame = None) -> np.ndarray:

    model_pipeline = load_pipeline()

    # Preprocess the new data and make a prediction
    y_pred = model_pipeline.predict(X_pred)

    print("\n🔮 prediction done", y_pred, y_pred.shape)

    return y_pred


if __name__ == '__main__':
    try:
        preprocess_and_train()
        pred()
    except:
        import ipdb, traceback, sys
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
