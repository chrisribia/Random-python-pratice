import numpy as np
np.random.seed(0)
from sklearn import da

X = [[1, 2, 3, 2.5],[2.0,5.0,-1.0,2.0],[-1.5,2.7,3.3,-0.8]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons))

    def forward(self,inputs):
        self.output = np.dot(inputs ,  np.array(self.weights).T) + self.biases

    def wei(self):
        return self.weights


layer1 = Layer_Dense(3,4)
# layer1 = Layer_Dense(3,2)

layer1.forward(X)
print(layer1.output)
print(X)
print(layer1.wei())
