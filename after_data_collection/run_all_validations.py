import subprocess
import os

# List of validation scripts to run (in desired order)
scripts = [
    "validation/check_missing_values.py",
    "validation/check_duplicates.py",
    "validation/check_category_consistency.py",
    "validation/check_outliers.py",
    "validation/check_data_types_and_ranges.py",
    "validation/data_quality_report.py"
]

print("🔎 Running all data validation checks...\n")

for script in scripts:
    print(f"▶️ Running: {script}")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"⚠️ Error in {script}:\n{result.stderr}")
    print("-" * 80)

print("✅ All validations complete.")
