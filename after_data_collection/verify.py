import pandas as pd

samples = [
    "data/sample_firstk.csv",
    "data/sample_random.csv",
    "data/sample_stratified.csv"
]

for path in samples:
    df = pd.read_csv(path)
    print(f"{path} columns: {list(df.columns)}")
