import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Load .env and data
load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
CSV_FILE = os.getenv("CSV_FILE", "consumer_spending.csv")
df = pd.read_csv(os.path.join(DATA_DIR, CSV_FILE))

print("📊 Running Data Quality Report...\n")

# 1. Check for Repeated Rows
duplicate_count = df.duplicated().sum()
print(f"✅ Duplicate Rows: {duplicate_count}")

# 2. Correlation Matrix (Numerical Only)
numeric_cols = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_cols.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix of Numeric Features")
plt.tight_layout()

# Save plot
correlation_path = os.path.join("visualization", "correlation_matrix.png")
os.makedirs("visualization", exist_ok=True)
plt.savefig(correlation_path)
print(f"✅ Correlation matrix saved to: {correlation_path}")
plt.close()

# 3. Data Error Rates
def error_rate(series):
    if series.dtype == "object":
        return series.isnull().mean() + (series == "").mean()
    elif np.issubdtype(series.dtype, np.number):
        return series.isnull().mean() + (series < 0).mean()
    return series.isnull().mean()

error_rates = df.apply(error_rate)
error_report = pd.DataFrame({
    "Column": error_rates.index,
    "ErrorRate (%)": (error_rates.values * 100).round(2)
})

print("\n🧪 Error Rates by Column:")
print(error_report.to_string(index=False))
