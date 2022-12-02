from sklearn.preprocessing import MinMaxScaler,FunctionTransformer
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.compose import ColumnTransformer, make_column_transformer, make_column_selector
import numpy as np
import pandas as pd

# #from chifoumy.ml_logic.encoders import (transform_time_features,
#                                               transform_lonlat_features,
#                                               compute_geohash)

def preprocess_features(X: pd.DataFrame) -> np.ndarray:

    def create_sklearn_preprocessor() -> ColumnTransformer:

        normalizer = FunctionTransformer(lambda x: (x - x.mean()) / x.std(), axis =1)
        scaling = make_column_transformer((MinMaxScaler(), make_column_selector(dtype_include=['float64'])))

        preprocess = make_pipeline(normalizer, scaling)
        return preprocess


    preprocessor = create_sklearn_preprocessor()

    X_processed = preprocessor.fit_transform(X)

    print("\n✅ X_processed, with shape", X_processed.shape)

    return X_processed
