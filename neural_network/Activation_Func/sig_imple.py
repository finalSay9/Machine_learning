import numpy as np
import Sigmod_fun
from Sigmod_fun import Sigmod


class SigmImplementation(Sigmod):

   #class attributes
    inputs = [1, -2, 1.0, 1.9],
      

    weights = [0.1, 0.2, -1, 0.5],
        
        
    
    bias1 = [1, 2, 3]
    sum = 0

    def __init__(self):
     pass

    #the forward passs
    def forward(self):
       for i in zip(self.inputs, self.weights):
          result = self.inputs[i] * self.weights[i]
          sum += result
          super().sig_forward(sum)
          return sum


obj1 = SigmImplementation()
print(obj1.forward())         
