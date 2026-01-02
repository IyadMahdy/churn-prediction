import json
import joblib
import pandas as pd

from catboost import CatBoostClassifier
from src.models.evaluation import evaluate_model

from sklearn.model_selection import train_test_split

from src.utils.config import PROCESSED_DATA_PATH, MODELS_DIR


def train_catboost(
    input_filename: str,
    model_filename: str,
    metrics_filename: str,
) -> dict:
    """
    Train a tuned CatBoost model using fixed hyperparameters
    identified during prior notebook-based experimentation.
    """

    # Load processed dataset
    df = pd.read_csv(PROCESSED_DATA_PATH / input_filename)

    X = df.drop(columns=["Churn", "customerID"])
    y = df["Churn"]

    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42,
    )

    best_params = {
        "iterations": 400,
        "learning_rate": 0.05,
        "depth": 4,
        "l2_leaf_reg": 7,
        "subsample": 0.7,
    }

    model = CatBoostClassifier(
        **best_params,
        eval_metric="AUC",
        auto_class_weights="Balanced",
        random_seed=42,
        logging_level="Silent",
        allow_writing_files=False
    )

    model.fit(X_train, y_train)

    metrics = evaluate_model(model, X_val, y_val)

    model_dir = MODELS_DIR / "catboost"
    model_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, model_dir / model_filename)

    with open(model_dir / metrics_filename, "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics


if __name__ == "__main__":
    results = train_catboost(
        input_filename="telco_customer_churn_selected_features.csv",
        model_filename="catboost_tuned.joblib",
        metrics_filename="catboost_metrics.json",
    )

    print("CatBoost training completed.")
    print("ROC-AUC:", results["roc_auc"])
