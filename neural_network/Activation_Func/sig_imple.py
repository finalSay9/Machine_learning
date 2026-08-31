import numpy as np
import Sigmod_fun


class SigmImplementation(Sigmod_fun):
    
    def __init__(self, inputs, weights, biases):
        self.inputs = inputs
        self.weights = weights
        self.biases = biases
