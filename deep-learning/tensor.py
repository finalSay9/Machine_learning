import numpy as np

inputs = [
    [1,-2,1.0,1.9],
    [2.1,0,1.1,3],
    [0.1,-3,5,1.0],
    [2.1,2,4.1,0.0]
    ]

weights = [
    [0.1,0.2,-1,0.5],
    [1.0,0.3,0.1,1.1],
    [1,3,4,5],
    [2,0,-1.2,-1,3]
]
weights = np.array(weights).T
calc = np.dot(inputs, weights)
print(calc)