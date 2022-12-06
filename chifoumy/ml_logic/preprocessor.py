import pandas as pd
from sklearn.preprocessing import FunctionTransformer, MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer, make_column_transformer, make_column_selector

def normalise(df:pd.DataFrame):
    return df.apply(lambda row: (row-row.mean()) / row.std(), axis=1)

def preprocess_features(df:pd.DataFrame):
    normalizer = FunctionTransformer(normalise)
    scaling = make_column_transformer((MinMaxScaler(), make_column_selector(dtype_include=['float64'])))

    return make_pipeline(normalizer, scaling)
