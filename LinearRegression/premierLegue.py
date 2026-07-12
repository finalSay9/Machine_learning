import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


#loading the csv into pandas dataframe
df = pd.read_csv('games.csv')

#now select your Feature matrix (X) and target vector y
X = df[['games_played','games_won', 'games_draw', 'games_lost']]

#now lets come to y(predicted value) and should be 1D
y = df['total_points']

#oky now lets initialize the empty model
model = LinearRegression(positive=True)

#train the model
model.fit(X, y)

# 4. Look at the math the model learned
print("Intercept (c):", model.intercept_)
print("Coefficients (m for each feature):", model.coef_)

# 5. Predict points for a new team
# Let's predict for a team with 20 played, 10 wins, 4 draws, and 6 losses
new_team_stats = [[20, 17, 4, 6]]
prediction = model.predict(new_team_stats)
print(f"Predicted total points: {prediction[0]:.1f}")
