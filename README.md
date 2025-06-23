# consumer_spending
Generates a synthetic consumer spending dataset in CSV and Parquet formats with sampling methods (First-K, Random, Stratified). Ideal for ML data preparation workflows in Amazon SageMaker. Modular Python scripts for easy integration into feature engineering and preprocessing pipelines.

# Consumer Spending ML Dataset & Sampling Project
This project provides a synthetic consumer spending dataset and demonstrates multiple data sampling strategies — ideal for machine learning pipelines in Amazon SageMaker or other data science environments.

It is designed to support the data preparation phase of ML workflows, especially for experimentation, testing, or demonstration of end-to-end ML pipelines.

# 🔧 Features
 - ✅ Generates realistic synthetic consumer spending data
 - ✅ Saves the dataset in both CSV and Parquet formats
 - ✅ Implements common sampling techniques:

# First-K Sampling

# Random Sampling

# Stratified Sampling (by spending category)

# ✅ Modular Python code for easy integration with ML pipelines (e.g., SageMaker Processing)

# 📂 Project Structure
```bash
consumer_spending_project/
├── data/                        # Generated CSV, Parquet, and samples
├── generate_dataset.py         # Creates the dataset
├── sample_methods.py           # Sampling logic
└── requirements.txt            # Python dependencies
```bash
# 📈 Use Case
- This project is ideal for:
  - Machine learning feature engineering pipelines
  - Demonstrating data preprocessing in Amazon SageMaker
  - Teaching or testing ML sampling techniques

# Objective of Sampling techniques
- To demonstrate data sampling techniques that are commonly used in ML workflows to:
  - Reduce data volume for prototyping
  - Maintain statistical integrity
  - Speed up pipeline iteration
  - Avoid bias or class imbalance


# Techniques and Their Use Cases
```bash
Technique	            Description & Use Case
First-K	                Quickly inspect the top k rows — useful for previewing structure or debugging
Random Sample	        Selects k rows randomly — helps in unbiased model testing or prototyping
Stratified Sample	    Samples a fraction from each category — used when class balance is important (e.g., fraud detection)

Each sampled dataset is saved to:
 - sample_firstk.csv
 - sample_random.csv
 - sample_stratified.csv
```

## 📊 Understanding Sampling Visualization

Below is a comparison of category distributions under three different sampling techniques:

![Sampling Comparison](./visualization/category%20comparision.png)

### 🔍 Interpretation

| Sampling Method   | Description                                                                 | Balanced? | Suitable for ML? |
|-------------------|-----------------------------------------------------------------------------|-----------|------------------|
| **First-K**        | Picks the first K rows. If data is ordered (e.g., by date), this introduces bias. | ❌ No      | 🚫 No             |
| **Random**         | Picks K random rows from the entire dataset. Distribution depends on original data. | ⚠️ Moderate | ✅ Yes            |
| **Stratified**     | Picks a percentage of rows from each category. Maintains distribution across groups. | ✅ Yes     | ✅ Best           |

### 🧠 Key Takeaways

- **First-K Sampling** is fast but biased.
- **Random Sampling** is better, but can reflect original imbalances.
- **Stratified Sampling** ensures every category is fairly represented — ideal for classification tasks.

> 🛠 Make sure your plots preserve the `Category` column and fix X-axis labels if numeric placeholders appear.
