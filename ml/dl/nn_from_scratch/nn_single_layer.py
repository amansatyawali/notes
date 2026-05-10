import numpy as np
from activations import Sigmoid, Tanh
from layers import Dense
import pandas as pd
from utils import split_xy, preprocess_y, preprocess_x, calculate_cost, derivative_log_loss, accuracy_score_from_probability
from sklearn.model_selection import train_test_split


DATA_PATH = "data/Invistico_Airline.csv"

##Get the data and preprocess
raw_df = pd.read_csv(DATA_PATH)
main_df = raw_df.copy()

X, Y = split_xy(main_df)

X = preprocess_x(X)
Y = preprocess_y(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=0)
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.1, random_state=0)

input_size = len(X_train.columns)
batch_size = 1

layer = Dense(input_size=input_size, output_size=1, activation_function=Sigmoid())


y_pred = layer.forward(X_test.T).T
print(calculate_cost(y_actual=Y_test, y_pred=y_pred))
print(accuracy_score_from_probability(y_actual = Y_test, y_pred=y_pred))
for i in range(10):

    idx = 0
    while idx < X_train.shape[0]:
    # while idx < 10:
        batch_number = idx/batch_size
        if batch_number%10000 ==0:
            print("Batch ",batch_number)
        batch_input = X_train.iloc[idx:idx + batch_size, :].to_numpy()
        batch_input_actual = Y_train.iloc[idx:idx + batch_size].to_numpy()

        output = layer.forward(batch_input.T).T
        change_wrt_output = derivative_log_loss(y_actual=batch_input_actual, y_pred=output)
        layer.back(batch_input_actual, derivative=change_wrt_output, learning_rate=0.01)
        cost = calculate_cost(y_actual= batch_input_actual, y_pred=output)
        idx += batch_size


y_pred = layer.forward(X_test.T).T
print(calculate_cost(y_actual=Y_test, y_pred=y_pred))
print(accuracy_score_from_probability(y_actual = Y_test, y_pred=y_pred))