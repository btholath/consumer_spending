import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

# Resolve paths relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, os.getenv("DATA_DIR", "data"))
CSV_FILE = os.getenv("CSV_FILE", "consumer_spending.csv")
VIS_DIR = os.path.join(BASE_DIR, "visualization")

# Ensure visualization folder exists
os.makedirs(VIS_DIR, exist_ok=True)

# Load data
df = pd.read_csv(os.path.join(DATA_DIR, CSV_FILE))

# Create the plot
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Category", order=df["Category"].value_counts().index)
plt.title("Transaction Count by Category")
plt.ylabel("Count")
plt.xlabel("Spending Category")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plot_path = os.path.join(VIS_DIR, "category_distribution.png")
plt.savefig(plot_path)
print(f"✅ Plot saved to {plot_path}")

# Optional: also show the plot
plt.show()
