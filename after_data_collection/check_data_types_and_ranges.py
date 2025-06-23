import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "data")
CSV_FILE = os.getenv("CSV_FILE", "consumer_spending.csv")
df = pd.read_csv(os.path.join(DATA_DIR, CSV_FILE))

print("🟣 Data Types:")
print(df.dtypes)

# Basic sanity checks
if df["Age"].min() < 0 or df["Age"].max() > 120:
    print("⚠️ Age out of expected range (0-120)")
if df["Income"].min() < 0:
    print("⚠️ Income should not be negative")
if df["Spending"].min() < 0:
    print("⚠️ Spending should not be negative")
