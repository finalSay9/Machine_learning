from nnfs.datasets import spiral_data
import numpy as np
import random

class Dense_layer:
    def __init__(self, n_inputs, n_nuerons):
        #initialize weights and biases
        #Guassian distribution
        """
        n_inputs represent the number of rows and
        the n_neurons represent the number of columns in the
        weight matrix
        """
        self.weights = 0.01 * np.random.randn(n_inputs, n_nuerons)
        self.biases = np.zeros((1, n_nuerons))
        



    def forward_pass(self,inputs):
        """
        calculate output values
        from inputs, weights and biases
        """
        pass


