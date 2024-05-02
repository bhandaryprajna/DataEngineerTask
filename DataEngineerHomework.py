import pandas as pd
import logging

def check_duplicates(df, columns):
    """
    Check for duplicates in a dataframe based on specified columns.

    Args:
    - df (pandas.DataFrame): The dataframe to check for duplicates.
    - columns (list): A list of columns on which to check for duplicates.

    Returns:
    - dict: A dictionary containing the count of duplicate cases and a dataframe with group count of duplicate rows.
    """
    # Validate input DataFrame and columns
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame")
    if not isinstance(columns, list):
        raise ValueError("Input 'columns' must be a list")
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame")

    # Find duplicates
    duplicates = df.duplicated(subset=columns, keep='first')

    # Count duplicates
    duplicate_count = duplicates.sum()

    # Get samples dataframe
    samples_df = df[duplicates].groupby(columns).size().reset_index(name='number_of_duplicates')
    # Print count and samples
    print("Duplicate Count:", duplicate_count, "Samples DataFrame:")
    print(samples_df)
    return {'count': duplicate_count, 'samples': samples_df}
    

