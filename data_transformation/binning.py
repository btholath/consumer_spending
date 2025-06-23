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

bins = [0, 25, 45, 65, 100]
labels = ["Young", "Adult", "Middle Age", "Senior"]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)

logging.info("✅ Binned Age into categories: %s", labels)

out_path = os.path.join(DATA_DIR, "binned.csv")
df.to_csv(out_path, index=False)
logging.info("✅ Saved to %s", out_path)