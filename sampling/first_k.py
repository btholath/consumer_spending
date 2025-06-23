"""
first_k.py

Provides a function to return the first K rows from a DataFrame.
"""

def first_k_sample(df, k=100):
    """
    Returns the first k rows from the input DataFrame.

    Parameters:
        df (pd.DataFrame): Input dataset.
        k (int): Number of rows to return from the top.

    Returns:
        pd.DataFrame: Subset of the first k rows.
    """
    return df.head(k)
