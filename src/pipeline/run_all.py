import argparse

from src.pipeline.ingest import run_ingestion
from src.pipeline.preprocess import run_preprocessing
from src.pipeline.features import run_feature_pipeline
from src.pipeline.train import run_training


def run_full_pipeline(models: list[str] | None = None):
    """
    Run the full end-to-end ML pipeline.
    """
    run_ingestion()
    run_preprocessing()
    run_feature_pipeline()
    run_training(models=models)

    print("Full ML pipeline completed successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the full churn prediction ML pipeline"
    )

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

    run_full_pipeline(models=args.model)
