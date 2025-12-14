from pathlib import Path
import pandas as pd
from src.utils.config import RAW_DATA_PATH, PROCESSED_DATA_PATH


def load_raw_data(filename: str) -> pd.DataFrame:
    """Load raw data from a CSV file.

    Args:
        filename (str): The name of the CSV file to load.

    Returns:
        pd.DataFrame: The loaded raw data as a pandas DataFrame.
    """

    file_path = RAW_DATA_PATH / filename

    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    return pd.read_csv(file_path)


def validate_data(df: pd.DataFrame, required_columns: list | None = None) -> None:
    """Validate that the DataFrame contains the required columns.

    Args:
        df (pd.DataFrame): The DataFrame to validate.
        required_columns (list, optional): A list of required column names. Defaults to None.

    Returns:
        None
    """

    if required_columns is None:
        required_columns = [
            "customerID",
            "gender",
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "tenure",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod",
            "MonthlyCharges",
            "TotalCharges",
            "Churn",
        ]

    missing_columns = set(required_columns) - set(df.columns)

    if df.empty:
        raise ValueError("The DataFrame is empty.")

    if missing_columns:
        raise ValueError(
            f"The following required columns are missing: {missing_columns}"
        )


def save_processed_data(
    df: pd.DataFrame, filename: str, dirname: str | None = None
) -> None:
    """Save processed data to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        filename (str): The name of the CSV file to save.
        dirname (str, optional): The directory name under PROCESSED_DATA_PATH. Defaults to None.

    Returns:
        None
    """

    if dirname:
        save_path = PROCESSED_DATA_PATH / dirname
    else:
        save_path = PROCESSED_DATA_PATH

    save_path.mkdir(parents=True, exist_ok=True)
    file_path = save_path / filename
    df.to_csv(file_path, index=False)


def ingest_data(
    filename: str,
    processed_filename: str,
    dirname: str | None = None,
    required_columns: list | None = None,
) -> pd.DataFrame:
    """Ingest data by loading, validating, and saving it.

    Args:
        filename (str): The name of the raw CSV file to load.
        processed_filename (str): The name of the processed CSV file to save.
        dirname (str, optional): The directory name under PROCESSED_DATA_PATH. Defaults to None.
        required_columns (list, optional): A list of required column names. Defaults to None.

    Returns:
        pd.DataFrame: The validated DataFrame.
    """

    df = load_raw_data(filename)
    validate_data(df, required_columns)
    save_processed_data(df, processed_filename, dirname)
    return df


if __name__ == "__main__":
    try:
        data = ingest_data(
            "telco_customer_churn.csv", "telco_customer_churn_validated.csv"
        )
        print("Data ingestion completed successfully. Shape:", data.shape)
    except Exception as e:
        print(f"An error occurred during data ingestion: {e}")
