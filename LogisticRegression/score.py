import pandas as pd



data = pd.read_csv('../datasets/student.csv')

placement_status  = data['placement_status'].value_counts()
print(data.info())