import numpy as np

class Sigmod():

    def __init__(self, x):
        self.x = x

    def sig_forward(self, value):
        #numerically stable sigmod
        return np.where(
            value >= 0,
            1 / (1 + np.exp(-value)),
            np.exp(value) / (1 + np.exp(value))
        )