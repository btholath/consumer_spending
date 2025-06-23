# data_transformation/minmax_scaling.py
import pandas as pd
import numpy as np
import os
import logging
from dotenv import load_dotenv
from sklearn.preprocessing import MinMaxScaler

# Setup
load_dotenv()
logging.basicConfig(level=logging.INFO)

DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"
path = os.path.join(DATA_DIR, FILE)

df = pd.read_csv(path)
scaler = MinMaxScaler()

columns = ["Age", "Income", "Spending"]
df[columns] = scaler.fit_transform(df[columns])
logging.info("✅ Applied Min-Max scaling to: %s", columns)

out_path = os.path.join(DATA_DIR, "minmax_scaled.csv")
df.to_csv(out_path, index=False)
logging.info("✅ Saved to %s", out_path)
