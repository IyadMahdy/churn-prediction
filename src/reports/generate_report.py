from datetime import datetime
import json
import joblib
import pandas as pd
from src.utils.config import MODELS_DIR, REPORTS_DIR, PROCESSED_DATA_PATH

EXPLANATIONS_PATH = REPORTS_DIR / "feature_explanations.json"


def explain_feature(feature_name: str, FEATURE_EXPLANATIONS: dict) -> str:
    """
    Retrieve a business-friendly explanation for a given feature.

    This function maps a feature name to its corresponding explanation
    derived from prior EDA and feature–target analysis. If no explanation
    is found, a default placeholder message is returned.

    Args:
        feature_name (str): Name of the feature.
        FEATURE_EXPLANATIONS (dict): Mapping of feature names to explanations.

    Returns:
        str: Explanation text for the feature.
    """
    return FEATURE_EXPLANATIONS.get(
        feature_name,
        (
            "This feature showed significant"
            " importance and requires further business analysis.",
        ),
    )


def load_feature_names():
    """
    Load feature names used for model training.

    Feature names are extracted from the final feature-selected dataset,
    excluding identifier and target columns.

    Returns:
        list[str]: List of feature names.
    """
    df = pd.read_csv(PROCESSED_DATA_PATH / "telco_customer_churn_selected_features.csv")
    return df.drop(columns=["Churn", "customerID"]).columns.tolist()


def extract_feature_importance(model_name: str):
    """
    Extract feature importance values from a trained model.

    The method used to extract feature importance depends on the model type:
    - Logistic Regression: model coefficients
    - Tree-based models: feature_importances_
    - CatBoost: built-in feature importance

    Args:
        model_name (str): Name of the model directory.

    Returns:
        pd.DataFrame: DataFrame containing features and their importance scores,
        sorted by absolute importance in descending order.
    """
    feature_names = load_feature_names()
    model_dir = MODELS_DIR / model_name

    model_file = next(model_dir.glob("*.joblib"))
    model = joblib.load(model_file)

    if model_name == "logistic_regression":
        importances = model.coef_[0]

    elif model_name in ["random_forest", "gradient_boosting"]:
        importances = model.feature_importances_

    elif model_name == "catboost":
        importances = model.get_feature_importance()

    else:
        raise ValueError(f"Unsupported model: {model_name}")

    importance_df = pd.DataFrame({"feature": feature_names, "importance": importances})

    importance_df["abs_importance"] = importance_df["importance"].abs()
    importance_df = importance_df.sort_values(by="abs_importance", ascending=False)

    return importance_df


def load_all_model_metrics():
    """
    Load evaluation metrics for all trained models.

    Metrics are read from JSON files stored in each model's directory.

    Returns:
        dict: Mapping of model names to their evaluation metrics.
    """
    model_results = {}

    for model_dir in MODELS_DIR.iterdir():
        if not model_dir.is_dir():
            continue

        metrics_files = list(model_dir.glob("*_metrics.json"))
        if not metrics_files:
            continue

        with open(metrics_files[0], "r") as f:
            metrics = json.load(f)

        model_results[model_dir.name] = metrics

    return model_results


def select_best_model(model_results: dict):
    """
    Select the best-performing model based on ROC-AUC score.

    Args:
        model_results (dict): Mapping of model names to evaluation metrics.

    Returns:
        str: Name of the model with the highest ROC-AUC score.
    """
    best_model = None
    best_auc = -1

    for model_name, metrics in model_results.items():
        auc = metrics.get("roc_auc", 0)
        if auc > best_auc:
            best_auc = auc
            best_model = model_name

    return best_model


def generate_report():
    """
    Generate an automated HTML report summarizing churn model performance.

    The report includes:
    - Automatic model selection based on ROC-AUC
    - Model performance metrics
    - Feature importance with business explanations
    - Final conclusions for stakeholders

    The output is saved as an HTML file in the reports directory.
    """
    all_models = load_all_model_metrics()
    best_model = select_best_model(all_models)
    metrics = all_models[best_model]

    roc_auc = metrics["roc_auc"]
    report = metrics["classification_report"]["1"]
    confusion_matrix = metrics["confusion_matrix"]

    importance_df = extract_feature_importance(best_model)
    top_features = importance_df.head(10).copy()

    with open(EXPLANATIONS_PATH, "r", encoding="utf-8") as f:
        FEATURE_EXPLANATIONS = json.load(f)

    top_features["explanation"] = top_features["feature"].apply(
        lambda x: explain_feature(x, FEATURE_EXPLANATIONS)
    )

    feature_blocks = ""

    for _, row in top_features.iterrows():
        feature_blocks += f"""
        <div style="margin-bottom:15px;">
            <strong>{row.feature}</strong><br>
            <small>{row.explanation}</small>
        </div>
        """

    today = datetime.now().strftime("%Y-%m-%d")

    html = f"""
    <html>
    <head>
        <title>Customer Churn Prediction Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f9f9f9;
            }}
            h1, h2 {{
                color: #2c3e50;
            }}
            .section {{
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.05);
            }}
            table {{
                border-collapse: collapse;
                width: 50%;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>

    <body>

        <h1>Customer Churn Prediction Report</h1>
        <p><strong>Date:</strong> {today}</p>
        <p><strong>Selected Model:</strong> {best_model.replace('_', ' ').title()}</p>

        <div class="section">
            <h2>Executive Summary</h2>
            <p>
                This report presents the results of a machine learning model developed
                to predict customer churn. After evaluating multiple models, Gradient
                Boosting was selected as the best-performing model based on ROC-AUC
                and recall for churned customers.
            </p>
        </div>

        <div class="section">
            <h2>Model Performance</h2>
            <p><strong>ROC-AUC:</strong> {roc_auc:.3f}</p>
            <p><strong>Precision (Churn):</strong> {report["precision"]:.3f}</p>
            <p><strong>Recall (Churn):</strong> {report["recall"]:.3f}</p>

            <h3>Confusion Matrix</h3>
            <table>
                <tr>
                    <th></th>
                    <th>Predicted No</th>
                    <th>Predicted Yes</th>
                </tr>
                <tr>
                    <th>Actual No</th>
                    <td>{confusion_matrix[0][0]}</td>
                    <td>{confusion_matrix[0][1]}</td>
                </tr>
                <tr>
                    <th>Actual Yes</th>
                    <td>{confusion_matrix[1][0]}</td>
                    <td>{confusion_matrix[1][1]}</td>
                </tr>
            </table>
        </div>

        <div class="section">
            <h2>Key Drivers of Customer Churn</h2>
            {feature_blocks}
        </div>

        <div class="section">
            <h2>Conclusion</h2>
            <p>
                The selected model demonstrates strong predictive performance and is
                suitable for identifying customers at high risk of churn. The results
                can support proactive retention strategies and targeted interventions.
            </p>
        </div>

    </body>
    </html>
    """

    REPORTS_DIR.mkdir(exist_ok=True)
    OUTPUT_FILE = REPORTS_DIR / "churn_model_report.html"
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    generate_report()
    print("Report generated successfully.")
