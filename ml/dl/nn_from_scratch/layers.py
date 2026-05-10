import numpy as np
import activations
from utils import log_loss, derivative_log_loss
import pandas as pd


class Dense:
    def __init__(self, input_size, output_size, activation_function=activations.Tanh()) -> None:
        
        normalization_value = 0.1
        self.weights = np.random.rand(output_size, input_size) * normalization_value
        self.bias = np.random.rand(output_size, 1) * normalization_value
        self.activation_function = activation_function


    def forward(self, input_batch) -> np.ndarray:
        self.input_batch = input_batch
        Z = np.matmul(self.weights, input_batch) + self.bias
        A = self.activation_function.forward(Z)
        self.output = A

        return self.output


    def back(self, Y_actual, derivative, learning_rate = 0.001) -> None:
        change_wrt_output = derivative

        change_wrt_z = self.activation_function.derivative * change_wrt_output

        batch_size = Y_actual.shape[0]
        input_mean = np.sum(self.input_batch, axis=1).reshape(1, -1)/batch_size
        change_wrt_weights = change_wrt_z * input_mean
        change_wrt_bias = change_wrt_z.reshape(-1, 1)

        change_wrt_input = (self.weights * change_wrt_z).sum(axis=0).reshape(1, -1).T

        self.weights = self.weights - change_wrt_weights * learning_rate
        self.bias = self.bias - change_wrt_bias * learning_rate

        return change_wrt_input
