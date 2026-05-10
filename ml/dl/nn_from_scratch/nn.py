from activations import Sigmoid, Tanh
from layers import Dense
from utils import derivative_log_loss

class NN:
    def __init__(self, layers):
        self.layers = []
        for layer_config in layers:
            self.layers.append(self._create_layer(layer_config))

    
    def _create_layer(self, layer_config):
        input_size = layer_config["input_size"]
        output_size = layer_config["output_size"]

        if layer_config["activation_function"] == "sigmoid":
            activation_function = Sigmoid()
        elif layer_config["activation_function"] == "tanh":
            activation_function = Tanh()
        else:
            raise ValueError(f'activation function not found - {layer_config["activation_function"]}')

        if layer_config["type"] == 'dense':
            layer = Dense(input_size=input_size, output_size=output_size, activation_function=activation_function)
        else: 
            raise ValueError(f'Layer type not found - {layer_config["type"]}')
        
        return layer
    
    def _forward(self, input_batch):

        output = input_batch
        for layer in self.layers:
            output = layer.forward(output)
        return output
    
    
    def _back(self, Y_actual, derivative, learning_rate):

        for layer in self.layers[::-1]:      #Going from last to first
            derivative = layer.back(Y_actual, derivative, learning_rate)
        pass
    
    
    def predict(self, input_batch):
        return self._forward(input_batch.T)
    

    def train_step(self, X, Y, learning_rate):
        Y_pred = self._forward(X.T)
        Y_pred = Y_pred.T           #To make pred same shape as actual
        derivative = derivative_log_loss(y_actual=Y, y_pred=Y_pred).reshape(1, 1)
        self._back(Y, derivative, learning_rate)


    def train_loop(self, num_epochs, X, Y, batch_size, learning_rate=0.01):
        for epoch in range(num_epochs):
            print("Epoch = ", epoch+1)
            idx = 0
            while idx < X.shape[0]:
                batch_input = X.iloc[idx:idx + batch_size, :].to_numpy()
                batch_input_actual = Y.iloc[idx:idx + batch_size].to_numpy()

                self.train_step(X=batch_input, Y=batch_input_actual, learning_rate=learning_rate)
                idx += batch_size