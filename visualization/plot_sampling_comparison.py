"""
plot_sampling_comparison.py

Compares category distribution across First-K, Random, and Stratified samples.
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
VIS_DIR = os.path.join(BASE_DIR, "visualization")

# Ensure visualization folder exists
os.makedirs(VIS_DIR, exist_ok=True)

# Load samples
firstk = pd.read_csv(f"{DATA_DIR}/sample_firstk.csv")
random = pd.read_csv(f"{DATA_DIR}/sample_random.csv")
stratified = pd.read_csv(f"{DATA_DIR}/sample_stratified.csv")

# Prepare plotting
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
samples = [firstk, random, stratified]
titles = ["First-K Sample", "Random Sample", "Stratified Sample"]

for ax, sample_df, title in zip(axes, samples, titles):
    sns.countplot(data=sample_df, x="Category", ax=ax,
                  order=sample_df["Category"].value_counts().index)
    ax.set_title(title)
    ax.set_ylabel("Count")
    ax.set_xlabel("Category")
    ax.tick_params(axis='x', rotation=45)

plt.suptitle("Category Distribution in Different Sampling Methods", fontsize=14)
plt.tight_layout()
# Save the plot
plot_path = os.path.join(VIS_DIR, "category comparision.png")
plt.savefig(plot_path)
print(f"✅ Plot saved to {plot_path}")
plt.show()
