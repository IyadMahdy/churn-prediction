import pandas as pd

from src.utils.config import PROCESSED_DATA_PATH


# ---------------------------------------------------------------------
# Feature Selection Configuration
# ---------------------------------------------------------------------

FEATURES_TO_DROP = [
    # Demographic and basic service indicators
    "gender",
    "Partner",
    "PhoneService",
    # Individual service subscription indicators (redundant)
    "MultipleLines_Yes",
    "MultipleLines_No phone service",
    "StreamingTV_Yes",
    "StreamingTV_No internet service",
    "StreamingMovies_Yes",
    "StreamingMovies_No internet service",
    "OnlineBackup_Yes",
    "OnlineBackup_No internet service",
    "DeviceProtection_Yes",
    "DeviceProtection_No internet service",
    "OnlineSecurity_No internet service",
    "TechSupport_No internet service",
    # Contract-related redundant features
    "Contract_One year",
    "Contract_Two year",
    # Tenure redundancy
    "tenure_bin",
    # Derived billing feature
    "TotalCharges",
    # Payment method features
    "PaymentMethod_Credit card (automatic)",
    "PaymentMethod_Mailed check",
]


def select_features(
    input_filename: str,
    output_filename: str,
) -> pd.DataFrame:
    """
    Apply final feature selection by removing redundant and low-value features.

    This function implements feature selection decisions derived from
    exploratory analysis, Mutual Information, and Logistic Regression-based
    importance assessment.

    The logic is design-driven and intentionally separated from analysis
    notebooks.

    Args:
        input_filename (str): Name of the feature-engineered input CSV file.
        output_filename (str): Name of the output CSV file after feature selection.

    Returns:
        pd.DataFrame: Dataset containing the selected feature set.
    """
    input_path = PROCESSED_DATA_PATH / input_filename
    df = pd.read_csv(input_path)

    # Drop selected features if present
    features_present = [col for col in FEATURES_TO_DROP if col in df.columns]
    df_selected = df.drop(columns=features_present)

    output_path = PROCESSED_DATA_PATH / output_filename
    df_selected.to_csv(output_path, index=False)

    return df_selected


if __name__ == "__main__":
    selected_df = select_features(
        input_filename="telco_customer_churn_feature_engineered.csv",
        output_filename="telco_customer_churn_selected_features.csv",
    )

    print(
        "Feature selection completed. Final shape:",
        selected_df.shape,
    )
