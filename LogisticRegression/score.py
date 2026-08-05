import pandas as pd
import numpy as np
from zlib import crc32

data = pd.read_csv("../datasets/student.csv")

#creating the stable id to be relied on
data["id"] = data.index

# Check the data
print(data.head())
print(data.columns)

# Target distribution
placement_status = data["placement_status"].value_counts()


def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

data.info()
print(placement_status)
print(data.describe())