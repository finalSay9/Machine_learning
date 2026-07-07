import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


#loading the csv into pandas dataframe
df = pd.read_csv('games.csv')

#now select your Feature matrix (X) and target vector y
X = df[['games_played', 'games_won', 'games_draw', 'games_lost']]

#now lets come to y(predicted value) and should be 1D
y = df['total_points']

#oky now lets initialize the empty model
model = LinearRegression()

#train the model
model.fit(X, y)

# 4. Look at the math the model learned
print("Intercept (c):", model.intercept_)
print("Coefficients (m for each feature):", model.coef_)