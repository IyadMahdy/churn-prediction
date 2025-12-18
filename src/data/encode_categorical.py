import pandas as pd

from src.utils.config import PROCESSED_DATA_PATH


def encode_categorical_features(
    input_filename: str,
    output_filename: str,
) -> pd.DataFrame:
    """
    Encode categorical features by:
    - Mapping binary categorical variables to 0/1
    - One-hot encoding multi-class categorical variables
    - Preserving all observations and numerical features

    Encoding decisions are informed by prior categorical inspection
    (see 05_categorical_data_cleaning.ipynb).

    Args:
        input_filename (str): Name of the processed input CSV file
        output_filename (str): Name of the encoded output CSV file

    Returns:
        pd.DataFrame: Encoded DataFrame ready for modeling
    """

    input_path = PROCESSED_DATA_PATH / input_filename
    df = pd.read_csv(input_path)

    # Separate target variable
    target_col = "Churn"
    y = df[target_col].map({"Yes": 1, "No": 0})

    X = df.drop(columns=[target_col])

    # Binary categorical feature mapping
    binary_mapping = {
        "Yes": 1,
        "No": 0,
        "Male": 1,
        "Female": 0,
    }

    binary_cols = [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "PaperlessBilling",
    ]

    for col in binary_cols:
        X[col] = X[col].map(binary_mapping)

    # Multi-class categorical features (One-Hot Encoding)
    multiclass_cols = [
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaymentMethod",
    ]

    X_encoded = pd.get_dummies(
        X,
        columns=multiclass_cols,
        drop_first=True,
    )

    # Reattach target variable
    df_encoded = pd.concat([X_encoded, y], axis=1)

    # Save encoded dataset
    output_path = PROCESSED_DATA_PATH / output_filename
    df_encoded.to_csv(output_path, index=False)

    return df_encoded


if __name__ == "__main__":
    encoded_df = encode_categorical_features(
        input_filename="telco_customer_churn_numeric_cleaned.csv",
        output_filename="telco_customer_churn_encoded.csv",
    )
    print("Categorical encoding completed. Shape:", encoded_df.shape)
