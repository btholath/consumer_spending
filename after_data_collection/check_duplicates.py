import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "data")
CSV_FILE = os.getenv("CSV_FILE", "consumer_spending.csv")
df = pd.read_csv(os.path.join(DATA_DIR, CSV_FILE))

dupes = df.duplicated().sum()
print(f"🟠 Duplicate rows found: {dupes}")
