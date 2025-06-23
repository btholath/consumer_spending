import pandas as pd
import os
from sklearn.preprocessing import StandardScaler, LabelEncoder
from dotenv import load_dotenv

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"
df = pd.read_csv(os.path.join(DATA_DIR, FILE))

# Encode categorical
df["Gender"] = LabelEncoder().fit_transform(df["Gender"])
df["Category"] = LabelEncoder().fit_transform(df["Category"])

# Scale numeric
scaler = StandardScaler()
df[["Age", "Income", "Spending"]] = scaler.fit_transform(df[["Age", "Income", "Spending"]])

print("✅ Data scaled and encoded for modeling.")
df.to_csv(os.path.join(DATA_DIR, "consumer_spending_transformed.csv"), index=False)
