from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4]]   # input
y = [30, 40, 50, 60]       # output

model = LinearRegression()
model.fit(X, y)

print(model.coef_)     # this is m
print(model.intercept_)# this is c