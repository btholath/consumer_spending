# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
from dotenv import load_dotenv

# Setup
load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
FILE = "consumer_spending.csv"
path = os.path.join(DATA_DIR, FILE)
df = pd.read_csv(path)

# Bar plot in pandas - Count by Category
df['Category'].value_counts().plot(kind='bar', title='Transaction Count by Category', xlabel='Category', ylabel='Count')
plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, "bar_plot.png"))
plt.clf()

# Pie chart in matplotlib - Gender distribution
gender_counts = df['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.axis('equal')
plt.savefig(os.path.join(DATA_DIR, "pie_chart.png"))
plt.clf()

# Box plots in seaborn - Spending by Category
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Category', y='Spending')
plt.title('Spending Distribution by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, "box_plot.png"))
plt.clf()

# Histograms with matplotlib - Income
plt.hist(df['Income'], bins=20, color='skyblue', edgecolor='black')
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, "histogram.png"))
plt.clf()

# Scatter plot in matplotlib - Income vs. Spending
plt.scatter(df['Income'], df['Spending'], alpha=0.6, edgecolors='w')
plt.title('Income vs. Spending')
plt.xlabel('Income')
plt.ylabel('Spending')
plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, "scatter_plot.png"))
plt.clf()

print("✅ All visualizations saved to the data directory.")