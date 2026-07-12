import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge


X = np.array([
    [1,3],
    [4,5],
    [7,7],
    [9,10]])
y = np.array([10,20,30,40])
osl = LinearRegression()
osl.fit(X,y)

print('ols coefficients: ', osl.coef_)

ridge = Ridge(alpha=1.0)
ridge.fit(X,y)
print('ridge coefficients: ', ridge.coef_)
print(ridge.predict([[2,5]]))