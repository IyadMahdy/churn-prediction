import json
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from src.models.evaluation import evaluate_model
from src.utils.config import PROCESSED_DATA_PATH, MODELS_DIR


def train_logistic_regression_baseline(
    input_filename: str,
    model_filename: str,
    scaler_filename: str,
    metrics_filename: str,
) -> dict:
    """
    Train and evaluate a Logistic Regression baseline model.

    Steps:
    - Load encoded dataset
    - Stratified train/validation split
    - Feature scaling
    - Train Logistic Regression with class_weight='balanced'
    - Evaluate basic classification metrics
    - Save model, scaler, and metrics

    This baseline is trained prior to feature engineering and feature selection
    and serves as a reference for subsequent models.
    """

    # Load data
    df = pd.read_csv(PROCESSED_DATA_PATH / input_filename)

    X = df.drop(columns=["Churn", "customerID"])
    y = df["Churn"]

    # Stratified split
    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42,
    )

    # Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)

    # Model
    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42,
    )
    model.fit(X_train_scaled, y_train)

    # Evaluation
    metrics = evaluate_model(model, X_val_scaled, y_val)

    # Save artifacts
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    # Create model-specific directory
    model_dir = MODELS_DIR / "logistic_regression"
    model_dir.mkdir(parents=True, exist_ok=True)

    # Save artifacts
    joblib.dump(
        model,
        model_dir / model_filename,
    )

    joblib.dump(
        scaler,
        model_dir / scaler_filename,
    )

    with open(model_dir / metrics_filename, "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics


if __name__ == "__main__":
    results = train_logistic_regression_baseline(
        input_filename="telco_customer_churn_selected_features.csv",
        model_filename="baseline.joblib",
        scaler_filename="baseline_scaler.joblib",
        metrics_filename="baseline_metrics.json",
    )

    print("Logistic Regression baseline training completed.")
    print("ROC-AUC:", results["roc_auc"])
