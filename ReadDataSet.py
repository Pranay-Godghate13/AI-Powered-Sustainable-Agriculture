import pandas as pd

def readDataSet(file_path):
    data=pd.read_csv(file_path)
    return data
