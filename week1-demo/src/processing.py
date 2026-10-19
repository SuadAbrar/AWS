import pandas as pd


def replace_placeholders(df: pd.DataFrame) -> pd.DataFrame:
    """Replace placeholder strings with pandas missing values."""
    placeholders = ['UNKNOWN', 'ERROR']
    return df.replace(placeholders, pd.NA)


def convert_column_types(df: pd.DataFrame) -> pd.DataFrame:
    """converting column types to appropriate data types."""
    cleaned_df = df.copy()

    numeric_columns = ['Quantity', 'Price Per Unit', 'Total Spent']
    for col in numeric_columns:
        cleaned_df[col] = pd.to_numeric(
            cleaned_df[col],
            errors='coerce'
        )

    cleaned_df["Transaction Date"] = pd.to_datetime(
        cleaned_df["Transaction Date"],
        format='%m-%d-%y',
        errors='coerce'
    )

    return cleaned_df


def report_missing_values(df: pd.DataFrame) -> pd.Series:
    """Report the number of missing values in each column."""
    return df.isna().sum()
