import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge


X = np.array([[1,1], [2,2.02],[3,3],[4.1,4.3]])
y = np.array([10,20,30,40])
osl = LinearRegression()
osl.fit(X,y)

print('ols coefficients: ', osl.coef_)

ridge = Ridge(alpha=1.0)
ridge.fit(X,y)
print('ridge coefficients: ', ridge.coef_)