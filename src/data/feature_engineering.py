import pandas as pd

from src.utils.config import PROCESSED_DATA_PATH


def add_tenure_bin(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a tenure-based categorical feature representing customer lifecycle stages.

    The feature groups customers into tenure intervals to capture non-linear
    churn behavior across different lifecycle phases. The upper bound is set
    dynamically to avoid hard-coded limits.

    Args:
        df (pd.DataFrame): Encoded customer dataset.

    Returns:
        pd.DataFrame: Dataset with an added 'tenure_bin' feature.
    """
    df = df.copy()

    max_tenure = df["tenure"].max()

    df["tenure_bin"] = pd.cut(
        df["tenure"],
        bins=[0, 6, 12, 24, max_tenure],
        labels=["0-6", "6-12", "12-24", "24+"],
        right=False,
    )

    return df


def add_num_active_services(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a feature counting the number of active subscribed services.

    This feature captures service adoption intensity, which reflects customer
    engagement and switching cost.

    Args:
        df (pd.DataFrame): Encoded customer dataset.

    Returns:
        pd.DataFrame: Dataset with an added 'num_active_services' feature.
    """
    df = df.copy()

    service_cols = [
        "OnlineSecurity_Yes",
        "OnlineBackup_Yes",
        "DeviceProtection_Yes",
        "TechSupport_Yes",
        "StreamingTV_Yes",
        "StreamingMovies_Yes",
    ]

    df["num_active_services"] = df[service_cols].sum(axis=1)

    return df


def add_is_month_to_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a binary feature indicating whether the customer is on a month-to-month contract.

    Customers without long-term contracts typically exhibit higher churn risk
    due to lower commitment.

    Args:
        df (pd.DataFrame): Encoded customer dataset.

    Returns:
        pd.DataFrame: Dataset with an added 'is_month_to_month' feature.
    """
    df = df.copy()

    contract_cols = [col for col in df.columns if col.startswith("Contract_")]

    df["is_month_to_month"] = (df[contract_cols].sum(axis=1) == 0).astype(int)

    return df


def add_is_auto_payment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a binary feature indicating automatic payment behavior.

    Automatic payment methods are associated with lower payment friction and
    stronger customer retention.

    Args:
        df (pd.DataFrame): Encoded customer dataset.

    Returns:
        pd.DataFrame: Dataset with an added 'is_auto_payment' feature.
    """
    df = df.copy()

    not_auto = [
        "PaymentMethod_Electronic check",
        "PaymentMethod_Mailed check",
    ]

    df["is_auto_payment"] = (df[not_auto].sum(axis=1) == 0).astype(int)

    return df


def build_feature_engineered_dataset(
    input_filename: str,
    output_filename: str,
) -> pd.DataFrame:
    """
    Apply approved feature engineering steps and persist the resulting dataset.

    This function augments the encoded dataset with engineered behavioral
    features that were validated during exploratory analysis.

    Args:
        input_filename (str): Name of the encoded input CSV file.
        output_filename (str): Name of the output CSV file with engineered features.

    Returns:
        pd.DataFrame: Feature-engineered dataset.
    """
    input_path = PROCESSED_DATA_PATH / input_filename
    df = pd.read_csv(input_path)

    df = add_tenure_bin(df)
    df = add_num_active_services(df)
    df = add_is_month_to_month(df)
    df = add_is_auto_payment(df)

    output_path = PROCESSED_DATA_PATH / output_filename
    df.to_csv(output_path, index=False)

    return df


if __name__ == "__main__":
    df_fe = build_feature_engineered_dataset(
        input_filename="telco_customer_churn_encoded.csv",
        output_filename="telco_customer_churn_feature_engineered.csv",
    )

    print("Feature engineering completed. Shape:", df_fe.shape)
