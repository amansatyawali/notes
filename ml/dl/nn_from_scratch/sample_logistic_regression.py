import pandas as pd
from utils import split_xy, preprocess_y, preprocess_x, calculate_cost, accuracy_score_from_probability
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss

DATA_PATH = "data/Invistico_Airline.csv"


raw_df = pd.read_csv(DATA_PATH)

main_df = raw_df.copy()

X, Y = split_xy(main_df)

X = preprocess_x(X)
Y = preprocess_y(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)

X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.1, random_state=42)

print(X_train.shape)
print(Y_train.shape)

lr = LogisticRegression()

lr.fit(X_train, Y_train)

Y_pred_test = lr.predict_proba(X_test)[... , 1]

print(calculate_cost(y_actual=Y_test, y_pred=Y_pred_test))

print(log_loss(y_true = Y_test, y_pred=Y_pred_test))
print(accuracy_score_from_probability(y_actual = Y_test, y_pred=Y_pred_test))
