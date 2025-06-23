# data_cleaning/remove_outliers_iqr.py
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"

path = os.path.join(DATA_DIR, FILE)
df = pd.read_csv(path)

def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]

for col in ["Age", "Income", "Spending"]:
    before = len(df)
    df = remove_outliers_iqr(df, col)
    after = len(df)
    print(f"✅ {col}: Removed {before - after} outliers")

df.to_csv(path, index=False)
