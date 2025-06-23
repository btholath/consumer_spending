# data_cleaning/fuzzy_match_categories.py
import pandas as pd
import os
from dotenv import load_dotenv
from fuzzywuzzy import process

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"

EXPECTED = ["Groceries", "Electronics", "Clothing", "Travel", "Healthcare"]

path = os.path.join(DATA_DIR, FILE)
df = pd.read_csv(path)

def fuzzy_fix(value):
    if pd.isna(value): return "Unknown"
    best, score = process.extractOne(value, EXPECTED)
    return best if score >= 80 else value

df["Category"] = df["Category"].apply(fuzzy_fix)
print("✅ Applied fuzzy matching to Category column.")
df.to_csv(path, index=False)
