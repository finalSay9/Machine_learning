import numpy as np
import Sigmod_fun


class SigmImplementation(Sigmod_fun):

   #class attributes
    inputs = [
        [1, -2, 1.0, 1.9],
        [2.1, 0, 1.1, 3],
        [0.1, -3, 5, 1.0],
    
        ]

    weights = [
        [0.1, 0.2, -1, 0.5],
        [1.0, 0.3, 0.1, 1.1],
        [1, 3, 4, 5],
        
    ]
    bias1 = [1, 2, 3]

    def __init__(self):
     pass
