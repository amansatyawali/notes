import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


def split_xy(input_df) -> pd.DataFrame:

    input_df = input_df[input_df["Arrival Delay in Minutes"].isna() == False]

    Y = input_df[['satisfaction']]
    X = input_df.drop(['satisfaction'], axis=1)

    return X, Y


def preprocess_y(Y) -> pd.DataFrame:
    Y['satisfaction'] = Y['satisfaction'].apply(lambda x : 1 if x == 'satisfied' else 0)
    return Y['satisfaction']


def preprocess_x(X) -> pd.DataFrame:

    X_categorical = X[['Customer Type', 'Type of Travel', 'Class']]
    X_numerical = X.drop(['Customer Type', 'Type of Travel', 'Class'], axis=1)

    scaler = StandardScaler(copy=False)
    X_numerical = pd.DataFrame(scaler.fit_transform(X_numerical))
    X_numerical.columns = scaler.get_feature_names_out()

    enc = OneHotEncoder(handle_unknown='ignore', feature_name_combiner='concat')
    X_categorical = pd.DataFrame(enc.fit_transform(X_categorical).toarray())
    X_categorical.columns = enc.get_feature_names_out()

    X = pd.concat([X_numerical, X_categorical], axis=1)

    return X


def _reshape_y_for_metrics(y):

    if isinstance(y, pd.Series):
        y = y.to_numpy().reshape(-1, 1)
    elif isinstance(y, pd.DataFrame):
        y = y.to_numpy().reshape(-1, 1)
    elif isinstance(y, np.ndarray):
        y = y.reshape(-1, 1)
    else:
        raise TypeError("y should be either a series or a ndarray")

    return y

def calculate_cost(y_actual, y_pred):

    y_pred = _reshape_y_for_metrics(y_pred)
    y_actual = _reshape_y_for_metrics(y_actual)

    assert y_pred.shape == y_actual.shape
    batch_size = y_pred.shape[0]
    if y_pred.any() == np.nan or y_pred.any() == 0:
        print(y_pred, y_actual)
    loss = - (np.log(y_pred) * y_actual + np.log(1-y_pred) * (1 - y_actual))

    cost = loss.sum()/batch_size
    return cost


def log_loss(y_actual, y_pred):
  
    np.seterr(divide = 'ignore') 
    y_pred = _reshape_y_for_metrics(y_pred)
    y_actual = _reshape_y_for_metrics(y_actual)

    assert y_pred.shape == y_actual.shape
    loss = - (np.log(y_pred) * y_actual + np.log(1-y_pred) * (1 - y_actual))

    return loss


def derivative_log_loss(y_actual, y_pred):
  
    y_pred = _reshape_y_for_metrics(y_pred)
    y_actual = _reshape_y_for_metrics(y_actual)

    assert y_pred.shape == y_actual.shape
    batch_size = y_pred.shape[0]
    # if y_pred.any() == np.nan or y_pred.any() == 1:
    derivative = - (y_actual / y_pred) + (1 - y_actual)/(1 - y_pred)
    derivative = np.sum(derivative, axis=0)/batch_size
    return derivative


def accuracy_score_from_probability(y_actual, y_pred):

    y_pred = _reshape_y_for_metrics(y_pred)
    y_actual = _reshape_y_for_metrics(y_actual)

    assert y_pred.shape == y_actual.shape
    y_pred =  np.where(y_pred > 0.5, 1, 0)
    return accuracy_score(y_true = y_actual, y_pred=y_pred)