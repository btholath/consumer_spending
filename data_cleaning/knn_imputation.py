# data_cleaning/knn_imputation.py
from sklearn.impute import KNNImputer
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"

path = os.path.join(DATA_DIR, FILE)
df = pd.read_csv(path)

numeric_cols = ["Age", "Income", "Spending"]
imputer = KNNImputer(n_neighbors=5)
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

print("✅ KNN imputation applied to numeric columns.")
df.to_csv(path, index=False)
