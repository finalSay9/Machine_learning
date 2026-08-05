import numpy as np

input1 = [1,2,3,4]
input2 = [2,1,3,0]

input1 = np.array([input1])
input2 = np.array([input2]).T
print(np.dot(input1, input2))