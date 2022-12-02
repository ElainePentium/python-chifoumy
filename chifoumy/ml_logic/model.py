#import pandas as pd
#from sklearn.model_selection import train_test_split ,cross_validate
#from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
#from sklearn.metrics import accuracy_score
from chifoumy.ml_logic.preprocessor import preprocess_features

# def split_sets (X, y):

#     X_train, X_test, y_train, y_test = train_test_split (X, y ,test_size = 0.3)
#     return X_train, X_test, y_train, y_test


def initialize_model() :

    model = SVC(kernel= 'poly', gamma = 1, coef0 = 0, C = 0.01, probability=True)
    return model

def pipeline_constructor () :

    pipeline = make_pipeline(preprocess_features(), initialize_model())
    return pipeline

def training(X, y):

    trained_model = pipeline_constructor().fit(X, y)
    return trained_model


# def cross_evaluate_model (X, y) :
#     X_train, y_train = split_sets(X , y)
#     pipe = training(X_train, y_train)
#     score = cross_validate(pipe, X_train, y_train, scoring='accuracy')
#     score['test_score'].mean()

#  def evaluate_model_metrics(model, X, y):
#     metrics = model.evaluate(
#         x=X,
#         y=y,
#         verbose=1,
#         return_dict=True)

#     loss = metrics["loss"]
#     accuracy = metrics["accuracy"]
#     print(f"\n✅ model evaluated: loss {round(loss, 2)}, accuracy {round(accuracy, 2)}")
#     return metrics

# def evaluate_model_perf (X , y):
#     X_train, y_train, X_test, y_test = split_sets(X , y)
#     pipe = training(X_train, y_train)
#     y_pred = pipe.predict(X_test)
#     accuracy_score(y_test, y_pred)
#     return accuracy_score
