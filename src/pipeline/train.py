import argparse

from src.models.train_logistic_regression import (
    train_logistic_regression_baseline,
)
from src.models.train_random_forest import (
    train_random_forest_baseline,
)
from src.models.train_gradient_boosting import (
    train_gradient_boosting,
)
from src.models.train_catboost import (
    train_catboost,
)


def run_training(models: list[str] | None = None):
    """
    Train selected models on the approved feature set.

    Args:
        models (list[str] | None):
            List of model names to train.
            If None, all models are trained.
    """
    input_file = "telco_customer_churn_selected_features.csv"

    # Model registry (single source of truth)
    model_registry = {
        "logistic_regression": lambda: train_logistic_regression_baseline(
            input_filename=input_file,
            model_filename="logistic_regression_baseline.joblib",
            scaler_filename="logistic_regression_baseline_scaler.joblib",
            metrics_filename="logistic_regression_baseline_metrics.json",
        ),
        "random_forest": lambda: train_random_forest_baseline(
            input_filename=input_file,
            model_filename="random_forest_baseline.joblib",
            metrics_filename="random_forest_baseline_metrics.json",
        ),
        "gradient_boosting": lambda: train_gradient_boosting(
            input_filename=input_file,
            metrics_filename="gradient_boosting_metrics.json",
        ),
        "catboost": lambda: train_catboost(
            input_filename=input_file,
            model_filename="catboost_tuned.joblib",
            metrics_filename="catboost_metrics.json",
        ),
    }

    # If no model specified -> train all
    if models is None:
        models = list(model_registry.keys())

    for model_name in models:
        if model_name not in model_registry:
            raise ValueError(
                f"Unknown model '{model_name}'. "
                f"Available models: {list(model_registry.keys())}"
            )

        print(f"Training {model_name}...")
        model_registry[model_name]()

    print("Training pipeline completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train churn prediction models")

    parser.add_argument(
        "--model",
        nargs="*",
        help=(
            "Model(s) to train. "
            "If omitted, all models are trained. "
            "Options: logistic_regression, random_forest, "
            "gradient_boosting, catboost"
        ),
    )

    args = parser.parse_args()

    run_training(models=args.model)
