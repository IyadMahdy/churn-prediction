import pandas as pd

from src.utils.config import PROCESSED_DATA_PATH


def clean_numeric_features(
    input_filename: str,
    output_filename: str,
) -> pd.DataFrame:
    """
    Clean numerical features by:
    - Converting TotalCharges to numeric
    - Handling missing numeric values
    - Preserving all observations

    Args:
        input_filename (str): Name of the processed input CSV file
        output_filename (str): Name of the cleaned output CSV file

    Returns:
        pd.DataFrame: Cleaned DataFrame
    """

    input_path = PROCESSED_DATA_PATH / input_filename
    df = pd.read_csv(input_path)

    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Impute with 0 since missing values correspond to customers with no tenure
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # Save cleaned dataset
    output_path = PROCESSED_DATA_PATH / output_filename
    df.to_csv(output_path, index=False)

    return df


if __name__ == "__main__":
    cleaned_df = clean_numeric_features(
        input_filename="telco_customer_churn_validated.csv",
        output_filename="telco_customer_churn_numeric_cleaned.csv",
    )
    print("Numeric cleaning completed. Shape:", cleaned_df.shape)
