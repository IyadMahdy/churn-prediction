import json
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

from src.models.evaluation import evaluate_model
from src.utils.config import PROCESSED_DATA_PATH, MODELS_DIR


def train_random_forest_baseline(
    input_filename: str,
    model_filename: str,
    metrics_filename: str,
) -> dict:
    """
    Train and evaluate a Random Forest baseline model.

    Steps:
    - Load feature-selected dataset
    - Stratified train/validation split
    - Train Random Forest classifier
    - Evaluate basic classification metrics
    - Save model and metrics

    This model serves as a baseline tree-based benchmark and is trained
    without feature scaling.
    """

    # Load data
    df = pd.read_csv(PROCESSED_DATA_PATH / input_filename)

    # Split features and target
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

    # Model
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    # Evaluation
    metrics = evaluate_model(model, X_val, y_val)

    # Save artifacts
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    model_dir = MODELS_DIR / "random_forest"
    model_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        model,
        model_dir / model_filename,
    )

    with open(model_dir / metrics_filename, "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics


if __name__ == "__main__":
    results = train_random_forest_baseline(
        input_filename="telco_customer_churn_selected_features.csv",
        model_filename="baseline.joblib",
        metrics_filename="baseline_metrics.json",
    )

    print("Random Forest baseline training completed.")
    print("ROC-AUC:", results["roc_auc"])
