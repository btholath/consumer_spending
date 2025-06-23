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
This project is ideal for:
Machine learning feature engineering pipelines
Demonstrating data preprocessing in Amazon SageMaker
Teaching or testing ML sampling techniques
