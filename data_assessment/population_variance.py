import pandas as pd
import numpy as np
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"
df = pd.read_csv(os.path.join(DATA_DIR, FILE))

columns = ["Age", "Income", "Spending"]
for col in columns:
    var = np.var(df[col])
    logging.info("✅ Population variance of %s: %.4f", col, var)