from sklearn.preprocessing import MinMaxScaler,FunctionTransformer
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.compose import ColumnTransformer, make_column_transformer, make_column_selector
import numpy as np
import pandas as pd

# #from chifoumy.ml_logic.encoders import (transform_time_features,
#                                               transform_lonlat_features,
#                                               compute_geohash)
def normalise(df : pd.DataFrame) -> pd.DataFrame:

        return df.apply(lambda raw: (raw-raw.mean()) / raw.std(), axis=1)



def preprocess_features() -> make_pipeline:

    normalizer = FunctionTransformer(normalise())
    scaling = make_column_transformer((MinMaxScaler(), make_column_selector(dtype_include=['float64'])))

    preprocessor = make_pipeline(normalizer, scaling)

    return preprocessor
