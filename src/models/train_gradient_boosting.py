import json
import joblib
import pandas as pd

from sklearn.ensemble import GradientBoostingClassifier
from src.models.evaluation import evaluate_model

from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_sample_weight

from src.utils.config import PROCESSED_DATA_PATH, MODELS_DIR


def train_gradient_boosting(input_filename: str, metrics_filename: str) -> dict:
    """
    Train a tuned Gradient Boosting model using fixed hyperparameters
    identified during prior notebook-based tuning.
    """

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

    sample_weight = compute_sample_weight(
        class_weight="balanced",
        y=y_train,
    )

    best_params = {
        "subsample": 0.8,
        "n_estimators": 100,
        "min_samples_leaf": 100,
        "max_depth": 2,
        "learning_rate": 0.1,
    }

    # 🔒 Fixed hyperparameters from tuning notebook
    model = GradientBoostingClassifier(
        **best_params,
        random_state=42,
    )

    model.fit(
        X_train,
        y_train,
        sample_weight=sample_weight,
    )

    metrics = evaluate_model(model, X_val, y_val)

    model_dir = MODELS_DIR / "gradient_boosting"
    model_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, model_dir / "gradient_boosting_tuned.joblib")

    with open(model_dir / "gradient_boosting_metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    with open(model_dir / metrics_filename, "w") as f:
        json.dump(metrics, f, indent=4)

    return metrics


if __name__ == "__main__":
    results = train_gradient_boosting(
        input_filename="telco_customer_churn_selected_features.csv",
    )

    print("Gradient Boosting training completed.")
    print("ROC-AUC:", results["roc_auc"])
