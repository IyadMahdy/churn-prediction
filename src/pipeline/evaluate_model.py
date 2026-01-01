import json
import joblib
import pandas as pd
from datetime import datetime

from src.models.evaluation import evaluate_model
from src.utils.config import PROCESSED_DATA_PATH, MODELS_DIR
import argparse


def run_evaluation(
    model_name: str,
    model_filename: str,
    input_filename: str,
    output_metrics_filename: str | None = None,
) -> dict:
    """
    Run evaluation for a trained model on the given dataset.

    This pipeline loads a saved model, evaluates it on the provided dataset,
    and stores evaluation metrics without retraining.
    """

    # Load dataset
    df = pd.read_csv(PROCESSED_DATA_PATH / input_filename)

    X = df.drop(columns=["Churn", "customerID"])
    y = df["Churn"]

    # Load trained model
    model_path = MODELS_DIR / model_name / model_filename
    model = joblib.load(model_path)

    # Evaluate
    metrics = evaluate_model(model, X, y)

    # Save metrics (do NOT overwrite training metrics)
    if output_metrics_filename is None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_metrics_filename = f"evaluation_metrics_{timestamp}.json"

    output_path = MODELS_DIR / model_name / output_metrics_filename
    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model evaluation pipeline")
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--model-file", required=True)
    parser.add_argument("--data-file", required=True)
    parser.add_argument(
        "--output-file",
        default=None,
        help="Optional output metrics file name (defaults to timestamped file)",
    )

    args = parser.parse_args()

    results = run_evaluation(
        model_name=args.model_name,
        model_filename=args.model_file,
        input_filename=args.data_file,
        output_metrics_filename=args.output_file,
    )

    print("Evaluation completed.")
    print("ROC-AUC:", results["roc_auc"])
