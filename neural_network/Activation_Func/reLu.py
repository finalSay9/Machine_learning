import numpy as np



class ReLu():
    #defining the init func
    def __init__(self, x):
        self.x = x

    def relu(self):
        return np.maximum(self.x, 0)