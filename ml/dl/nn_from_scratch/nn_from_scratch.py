from utils import split_xy, preprocess_y, preprocess_x, calculate_cost, accuracy_score_from_probability
from sklearn.model_selection import train_test_split
import pandas as pd
from nn import NN

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

net = NN(layers=[
    {"type": "dense", "input_size": input_size, "output_size": 4, "activation_function": "tanh"},
    # {"type": "dense", "input_size": 4, "output_size": 4, "activation_function": "tanh"},
    {"type": "dense", "input_size": 4, "output_size": 1, "activation_function": "sigmoid"}
])

y_pred = net.predict(X_test)
print(calculate_cost(y_actual=Y_test, y_pred=y_pred))
print(accuracy_score_from_probability(y_actual = Y_test, y_pred=y_pred))

net.train_loop(num_epochs=40, X=X_train, Y=Y_train, batch_size=20, learning_rate=0.1)
net.train_loop(num_epochs=20, X=X_train, Y=Y_train, batch_size=1, learning_rate=0.1)
net.train_loop(num_epochs=40, X=X_train, Y=Y_train, batch_size=1, learning_rate=0.01)


y_pred = net.predict(X_test)
print(calculate_cost(y_actual=Y_test, y_pred=y_pred))
print(accuracy_score_from_probability(y_actual = Y_test, y_pred=y_pred))