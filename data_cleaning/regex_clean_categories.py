# data_cleaning/regex_clean_categories.py
import pandas as pd
import os
import re
from dotenv import load_dotenv

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"

path = os.path.join(DATA_DIR, FILE)
df = pd.read_csv(path)

def clean_category(value):
    if pd.isna(value):
        return "Unknown"
    value = re.sub(r"[^a-zA-Z]", "", value)  # remove special characters
    return value.strip().title()

df["Category"] = df["Category"].apply(clean_category)

print("✅ Cleaned category labels using regex.")
df.to_csv(path, index=False)
