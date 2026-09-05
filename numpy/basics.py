import numpy as np
import random



data = np.arange(16).reshape(4,4)
print(data)
print(data.shape)
print(data.ndim)
print(data.itemsize)

"""
creation of an array in numpy
sequences of sequences of sequences
"""

data_1 = np.array([1,2,3,4,5],
                  [6,7,8,9,0],
                  [9,0,7,1])
print(data_1)