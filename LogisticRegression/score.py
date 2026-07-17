import pandas as pd
import numpy as np

data = pd.read_csv("../datasets/student.csv")

# Check the data
print(data.head())
print(data.columns)

# Target distribution
placement_status = data["placement_status"].value_counts()

# Reproducible split
np.random.seed(42)

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(data, 0.2)

print(f"Training samples: {len(train_set)}")
print(f"Testing samples: {len(test_set)}")

data.info()
print(placement_status)
print(data.describe())