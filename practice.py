from sklearn.linear_model import LinearRegression

# a 4 by 1 matrix (that is 4 rows, 1 column)
X = [[1], [2], [3], [4]]   # input

# this is a 1 by 4 matrix, target vector
y = [30, 40, 50, 60]       # output

#
model = LinearRegression()
model.fit(X, y)

print(model.coef_)     # this is m
print(model.intercept_)# this is c