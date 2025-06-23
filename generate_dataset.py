"""
generate_dataset.py

— Purpose and Workflow
This script creates a synthetic consumer spending dataset to simulate real-world transactional behavior. 
The output is stored in both CSV and Parquet formats for compatibility with ML tools like Amazon SageMaker, pandas, PySpark, etc.
"""

import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
import os
from dotenv import load_dotenv

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
CSV_FILE = os.getenv("CSV_FILE")
PARQUET_FILE = os.getenv("PARQUET_FILE")

def generate_consumer_spending_data(n=1000):
    np.random.seed(42)
    data = {
        "CustomerID": np.arange(1, n + 1),
        "Age": np.random.randint(18, 70, size=n),
        "Gender": np.random.choice(["Male", "Female"], size=n),
        "Income": np.random.normal(60000, 15000, size=n).astype(int),
        "Category": np.random.choice(["Groceries", "Electronics", "Clothing", "Travel", "Healthcare"], size=n),
        "Spending": np.random.uniform(10, 1000, size=n).round(2),
        "TransactionDate": pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, size=n), unit='d')
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    df = generate_consumer_spending_data()

    df.to_csv(f"{DATA_DIR}/{CSV_FILE}", index=False)
    pq.write_table(pa.Table.from_pandas(df), f"{DATA_DIR}/{PARQUET_FILE}")
    print("✅ Dataset written to CSV and Parquet")
