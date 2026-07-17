import pandas as pd
import numpy as np
from zlib import crc32

data = pd.read_csv("../datasets/student.csv")

# Check the data
print(data.head())
print(data.columns)

# Target distribution
placement_status = data["placement_status"].value_counts()


def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

data.info()
print(placement_status)
print(data.describe())