import json
import joblib
import pandas as pd

from src.models.evaluation import evaluate_model
from src.utils.config import PROCESSED_DATA_PATH, MODELS_DIR
import argparse


def run_evaluation(
    model_name: str,
    model_filename: str,
    input_filename: str,
    output_metrics_filename: str = "evaluation_metrics.json",
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
    output_path = MODELS_DIR / model_name / output_metrics_filename
    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run model evaluation pipeline")
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--model-file", required=True)
    parser.add_argument("--data-file", required=True)

    args = parser.parse_args()

    results = run_evaluation(
        model_name=args.model_name,
        model_filename=args.model_file,
        input_filename=args.data_file,
    )

    print("Evaluation completed.")
    print("ROC-AUC:", results["roc_auc"])
