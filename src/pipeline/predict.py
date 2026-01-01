import argparse
import joblib
import pandas as pd

from src.utils.config import PROCESSED_DATA_PATH, MODELS_DIR


def run_prediction(
    model_name: str,
    model_filename: str,
    input_filename: str,
    output_filename: str = "predictions.csv",
) -> pd.DataFrame:
    """
    Run prediction for a trained model on the given dataset.

    This pipeline loads a saved model, generates churn probabilities
    and predictions, and saves the results as a CSV file.
    """

    # Load dataset
    df = pd.read_csv(PROCESSED_DATA_PATH / input_filename)

    # Keep customerID for output
    customer_ids = df["customerID"]

    # Drop non-feature columns if present
    drop_cols = ["customerID"]
    if "Churn" in df.columns:
        drop_cols.append("Churn")

    X = df.drop(columns=drop_cols)

    # Load trained model
    model_path = MODELS_DIR / model_name / model_filename
    model = joblib.load(model_path)

    # Generate predictions
    churn_probabilities = model.predict_proba(X)[:, 1]
    churn_predictions = model.predict(X)

    # Build predictions DataFrame
    predictions_df = pd.DataFrame(
        {
            "customerID": customer_ids,
            "churn_probability": churn_probabilities,
            "churn_prediction": churn_predictions,
        }
    )

    # Save predictions
    output_path = MODELS_DIR / model_name / output_filename
    predictions_df.to_csv(output_path, index=False)

    return predictions_df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model prediction pipeline")

    parser.add_argument("--model-name", required=True)
    parser.add_argument("--model-file", required=True)
    parser.add_argument("--data-file", required=True)
    parser.add_argument(
        "--output-file",
        default="predictions.csv",
        help="Name of the output predictions CSV file",
    )

    args = parser.parse_args()

    predictions = run_prediction(
        model_name=args.model_name,
        model_filename=args.model_file,
        input_filename=args.data_file,
        output_filename=args.output_file,
    )

    print("Prediction completed.")
    print(f"Saved {len(predictions)} predictions.")
