"""
plot_income_vs_spending.py

Shows the relationship between income and spending, grouped by category.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()
# Resolve paths relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.getenv("DATA_DIR", "data")
CSV_FILE = os.getenv("CSV_FILE")
VIS_DIR = os.path.join(BASE_DIR, "visualization")

# Ensure visualization folder exists
os.makedirs(VIS_DIR, exist_ok=True)

df = pd.read_csv(f"{DATA_DIR}/{CSV_FILE}")

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Income", y="Spending", hue="Category")
plt.title("Spending vs. Income by Category")
plt.xlabel("Income")
plt.ylabel("Spending")
plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
# Save the plot
plot_path = os.path.join(VIS_DIR, "income_vs_spending.png")
plt.savefig(plot_path)
print(f"✅ Plot saved to {plot_path}")
plt.show()
