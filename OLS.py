import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


X = np.array([
    [11,13],
    [14,15],
    [17,17],
    [19,20],
    [20,22]
])

y = np.array([110,120,130,140,150])

osl = LinearRegression()
osl.fit(X,y)

print('osl coefficients: ', osl.coef_)
print('osl intercept: ', osl.intercept_)

print('predict: ', osl.predict([[12,14]]))
