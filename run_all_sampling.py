import pandas as pd
import os
from dotenv import load_dotenv
from sampling.first_k import first_k_sample
from sampling.random_sample import random_sample
from sampling.stratified_sample import stratified_sample

load_dotenv()
DATA_DIR = os.getenv("DATA_DIR", "data")
CSV_FILE = os.getenv("CSV_FILE")
FIRST_K = int(os.getenv("FIRST_K", 100))
RANDOM_K = int(os.getenv("RANDOM_K", 100))
STRATIFIED_FRAC = float(os.getenv("STRATIFIED_FRAC", 0.2))

df = pd.read_csv(f"{DATA_DIR}/{CSV_FILE}", parse_dates=["TransactionDate"])

firstk = first_k_sample(df, FIRST_K)
firstk.to_csv(f"{DATA_DIR}/sample_firstk.csv", index=False)

random = random_sample(df, RANDOM_K)
random.to_csv(f"{DATA_DIR}/sample_random.csv", index=False)

stratified = stratified_sample(df, frac=STRATIFIED_FRAC)
stratified.to_csv(f"{DATA_DIR}/sample_stratified.csv", index=False)

print("✅ Sampling complete. Output files saved to /data/")
