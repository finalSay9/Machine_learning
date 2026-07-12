import numpy as np
from sklearn.linear_model import LinearRegression, Ridge

X = np.array([
    [11,21],
    [13,23],
    [17,17],
    [19,22],
    [20,22]
])

y = np.array([110,120,130,140,150])

ridge = LinearRegression()
ridge = Ridge(alpha=1.0)
ridge.fit(X,y)


print('coefficients: ', ridge.coef_)
print('intercept: ', ridge.intercept_)
print('predict: ', ridge.predict([[12,14]]))