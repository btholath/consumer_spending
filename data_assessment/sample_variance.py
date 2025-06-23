import pandas as pd
import os
import logging
from dotenv import load_dotenv
import statistics

load_dotenv()
logging.basicConfig(level=logging.INFO)

DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"
df = pd.read_csv(os.path.join(DATA_DIR, FILE))

columns = ["Age", "Income", "Spending"]
for col in columns:
    var = statistics.variance(df[col])
    logging.info("✅ Sample variance of %s: %.4f", col, var)