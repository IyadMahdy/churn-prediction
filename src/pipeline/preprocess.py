from src.data.clean_numeric import clean_numeric_features
from src.data.encode_categorical import encode_categorical_features


def run_preprocessing():
    """
    End-to-end preprocessing pipeline:
    - Numeric cleaning
    - Categorical encoding
    """
    clean_numeric_features(
        input_filename="telco_customer_churn_validated.csv",
        output_filename="telco_customer_churn_numeric_cleaned.csv",
    )

    df_encoded = encode_categorical_features(
        input_filename="telco_customer_churn_numeric_cleaned.csv",
        output_filename="telco_customer_churn_encoded.csv",
    )

    return df_encoded


if __name__ == "__main__":
    df = run_preprocessing()
    print("Preprocessing pipeline completed. Shape:", df.shape)
