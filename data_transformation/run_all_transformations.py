# data_transformation/run_all_transformations.py
import subprocess

scripts = [
    "data_transformation/zscore_scaling.py",
    "data_transformation/minmax_scaling.py",
    "data_transformation/binning.py",
    "data_transformation/unit_normalization.py",
    "data_transformation/rank_transform.py"
]

print("🚀 Running all data transformation scripts...\n")

for script in scripts:
    print(f"▶️ Running: {script}")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"⚠️ Error in {script}:", result.stderr)
    print("-" * 70)

print("✅ All transformations complete.")
