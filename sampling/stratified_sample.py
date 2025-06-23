"""
stratified_sample.py

Provides a function to perform stratified sampling based on a categorical column.
"""

def stratified_sample(df, stratify_col="Category", frac=0.2):
    """
    Returns a stratified sample from the input DataFrame.

    Parameters:
        df (pd.DataFrame): Input dataset.
        stratify_col (str): Column to stratify on (e.g., category, label).
        frac (float): Fraction of each stratum to sample (e.g., 0.2 = 20%).

    Returns:
        pd.DataFrame: Stratified sample of the dataset.
    """
    return df.groupby(stratify_col, group_keys=False)\
             .apply(lambda x: x.sample(frac=frac, random_state=42))\
             .reset_index(drop=True)
