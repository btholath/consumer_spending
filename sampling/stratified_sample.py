"""
stratified_sample.py

The function picks a small portion of data from each category in your consumer spending dataset — like taking a fair sample from each type of expense (e.g., Groceries, Travel, Electronics).
This helps ensure that your sample still represents all types of spending, even though it’s smaller than the full dataset.

Imagine you run a store and have 5 categories of purchases:
Groceries
Electronics
Clothing
Travel
Healthcare

Instead of looking at all 1,000 customer records, you want to study just 20% — but you want to make sure you include:

20% of Grocery buyers
20% of Electronics buyers
20% of each of the other groups

That way, you're not ignoring any one group, and your analysis stays balanced.

- End Result
 - You get a new smaller dataset (e.g., 200 rows from 1,000) that:
 - Still contains all types of spending
 - Maintains the same distribution of categories
 - Is ready to be used for training/testing machine learning models

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
    # This code will remove whichever stratify_col is passed from the output file
    #return df.groupby(stratify_col, group_keys=False)\
    #         .apply(lambda x: x.sample(frac=frac, random_state=42), include_groups=False)\
    #         .reset_index(drop=True)

    
    
    # Keep the stratify column explicitly in the result
    #grouped = df.groupby(stratify_col, group_keys=False)
    #
    # Explicitly drop grouping columns (future-proof)
    #sampled = grouped.apply(
    #    lambda x: x.sample(frac=frac, random_state=42),
    #    include_groups=False  # resolves FutureWarning
    #)
    # Ensure stratify_col is preserved (if not included automatically)
    #if stratify_col not in sampled.columns:
    #    sampled[stratify_col] = grouped.ngroup()  # fallback group index (not ideal)
    # 
    #return sampled.reset_index(drop=True)

    # Ensure the stratify column exists
    if stratify_col not in df.columns:
        raise ValueError(f"'{stratify_col}' column not found in DataFrame")

    # Perform stratified sampling
    grouped = df.groupby(stratify_col, group_keys=False)
    sampled = grouped.apply(
        lambda x: x.sample(frac=frac, random_state=42),
        include_groups=False  # Suppresses future warning
    )

    # Reset index and return
    return sampled.reset_index(drop=True)