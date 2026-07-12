from sklearn.linear_model import LogisticRegression
import pandas as pd

# ----------------------------
# Create Dataset
# ----------------------------

school_data = pd.DataFrame({
    "score": [40, 44, 66, 77, 90, 11, 70, 90, 88, 55, 66, 77, 88, 99],
    "pass":  [0,  0,  1,  1,  1,  0,  1,  1,  1,  0,  1,  1,  1,  1]
})

# ----------------------------
# Features (X) and Target (y)
# ----------------------------

X = school_data[["score"]]
y = school_data["pass"]

# ----------------------------
# Create and Train Model
# ----------------------------

logistic_model = LogisticRegression()
logistic_model.fit(X, y)

# ----------------------------
# New Students
# ----------------------------

new_scores = pd.DataFrame({
    "score": [35, 60, 90, 9]
})

# ----------------------------
# Predictions
# ----------------------------

predictions = logistic_model.predict(new_scores)
probabilities = logistic_model.predict_proba(new_scores)

# ----------------------------
# Display Results
# ----------------------------

results = new_scores.copy()

results["Prediction"] = predictions
results["Probability of Fail"] = probabilities[:, 0]
results["Probability of Pass"] = probabilities[:, 1]

print(results)