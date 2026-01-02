from src.features.feature_engineering import (
    build_feature_engineered_dataset,
)
from src.features.feature_selection import select_features


def run_feature_pipeline():
    """
    Feature pipeline:
    - Apply approved feature engineering
    - Apply final feature selection
    """
    build_feature_engineered_dataset(
        input_filename="telco_customer_churn_encoded.csv",
        output_filename="telco_customer_churn_feature_engineered.csv",
    )

    df_selected = select_features(
        input_filename="telco_customer_churn_feature_engineered.csv",
        output_filename="telco_customer_churn_selected_features.csv",
    )

    return df_selected


if __name__ == "__main__":
    df = run_feature_pipeline()
    print("Feature pipeline completed. Shape:", df.shape)
