import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data = pd.read_csv('../datasets/student.csv')

placement_status  = data['placement_status'].value_counts()

#setting aside the test set
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


plots = data.hist(bins=50, figsize=(20,15))
plt.show()
print(data.info())
print(placement_status)
print(data.describe())