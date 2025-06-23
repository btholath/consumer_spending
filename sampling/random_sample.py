"""
random_sample.py

Provides a function to perform random sampling from a DataFrame.
"""

def random_sample(df, k=100):
    """
    Returns k randomly selected rows from the input DataFrame.

    Parameters:
        df (pd.DataFrame): Input dataset.
        k (int): Number of random rows to select.

    Returns:
        pd.DataFrame: Randomly sampled subset of the data.
    """
    return df.sample(n=k, random_state=42)
