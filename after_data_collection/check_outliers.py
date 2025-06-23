import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "data")
CSV_FILE = os.getenv("CSV_FILE", "consumer_spending.csv")
df = pd.read_csv(os.path.join(DATA_DIR, CSV_FILE))

def detect_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return column[(column < lower) | (column > upper)]

for col in ["Age", "Income", "Spending"]:
    outliers = detect_outliers(df[col])
    print(f"🔴 Outliers in {col}: {len(outliers)}")
