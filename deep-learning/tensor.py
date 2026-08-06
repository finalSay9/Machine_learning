import numpy as np

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

weight1 = [
    [1, 2,  3.1],
    [1.0,  0.1, 0.0],
    [2, 3,  0]
    ]

biase1 = [0.1, 3.1, 2.0]

dot1 = np.dot(inputs, np.array(weights).T) + bias1
dot2 = np.dot(dot1, np.array(weight1).T) + biase1
print(dot2)
