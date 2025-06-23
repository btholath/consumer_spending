import subprocess

scripts = [
    "data_cleaning/knn_imputation.py",
    "data_cleaning/remove_outliers_iqr.py",
    "data_cleaning/regex_clean_categories.py",
    "data_cleaning/fuzzy_match_categories.py"
]

print("🧼 Running all data cleaning algorithms...\n")

for script in scripts:
    print(f"▶️ Executing: {script}")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"⚠️ Error in {script}:\n{result.stderr}")
    print("-" * 70)

print("✅ All data cleaning algorithms completed.")
