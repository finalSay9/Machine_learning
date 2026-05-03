from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()

dataset = pd.Series(np.random.rand(100)).to_list()

df = pd.DataFrame(dataset)

@app.get('/')
def data():
    return df[:2]