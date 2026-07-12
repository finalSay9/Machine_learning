from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np


#school data
school_data = pd.DataFrame({
    'score': [40,44,66,77,90,11,70,90,88,55,66,77,88,99],
    'pass': [0,0,1,1,1,0,1,1,1,0,1,1,1,1]
    })

model = LogisticRegression()
model.fit(school_data[['score']], school_data['pass']) 

#predict the exact category

new_score = [[35],[60],[90],[9]]
predictions = model.predict(new_scores)

print("Predicted Outcomes (0=Fail, 1=Pass):", predictions)
