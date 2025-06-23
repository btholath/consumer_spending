# data_transformation/rank_transform.py
import pandas as pd
import os
import logging
from dotenv import load_dotenv

# Setup
load_dotenv()
logging.basicConfig(level=logging.INFO)

DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"
path = os.path.join(DATA_DIR, FILE)

df = pd.read_csv(path)
columns = ["Age", "Income", "Spending"]

for col in columns:
    df[f"{col}_Rank"] = df[col].rank(method="average")
    logging.info("✅ Ranked column: %s", col)

out_path = os.path.join(DATA_DIR, "rank_transformed.csv")
df.to_csv(out_path, index=False)
logging.info("✅ Saved to %s", out_path)