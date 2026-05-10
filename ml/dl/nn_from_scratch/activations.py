import numpy as np


class Sigmoid:

    def forward(self, x) -> np.ndarray:
        batch_size = x.shape[1]
        output = 1/(1 + np.exp(-x))
        
        self.derivative = np.sum(output * (1 - output))/batch_size

        return output

    

class Tanh:

    def forward(self, x) -> np.ndarray:
        batch_size = x.shape[0]
        output =  (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))

        self.derivative = np.sum(1 - output **2)/batch_size

        return output
    

# class Relu:

#     def forward(self, x) -> np.ndarray:
#         batch_size = x.shape[1]
        
#         if x > 0:
#             output = x
#         else:
#             output = 0

#         return output