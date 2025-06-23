import pandas as pd
import os
from dotenv import load_dotenv

EXPECTED_CATEGORIES = ["Groceries", "Electronics", "Clothing", "Travel", "Healthcare"]

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "data")
CSV_FILE = os.getenv("CSV_FILE", "consumer_spending.csv")
df = pd.read_csv(os.path.join(DATA_DIR, CSV_FILE))

actual = sorted(df["Category"].dropna().unique())
print("🔵 Actual Categories:", actual)

extra = set(actual) - set(EXPECTED_CATEGORIES)
missing = set(EXPECTED_CATEGORIES) - set(actual)

if extra:
    print("⚠️ Unexpected categories:", extra)
if missing:
    print("⚠️ Missing expected categories:", missing)
