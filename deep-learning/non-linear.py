import nnfs
from nnfs.datasets import spiral_data
import numpy as np
import random

class Dense_layer:
    def __init__(self, n_inputs, n_neurons):
        #initialize weights and biases
        #Guassian distribution
        """
        n_inputs represent the number of rows and
        the n_neurons represent the number of columns in the
        weight matrix
        """
        self.weights = 0.01 * np.random.randn(
            n_inputs,
              n_neurons)
        """
        here 1 represent 1 row and n_neurons represent the number of
        columns in the biases
        """
        self.biases = np.zeros(
            (1, n_neurons)
            )

        



    def forward_pass(self,inputs):
        """
        calculate output values
        from inputs, weights and biases
        """
        self.inputs = np.dot(
            inputs, self.weights
            ) + self.biases

#create dataset
X,y = spiral_data(samples=100, classes=3)



"""
create a dense layer with 2 input
features and 3 output values
"""
dense1 = Dense_layer(2,3)






