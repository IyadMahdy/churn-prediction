from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_auc_score,
)


def evaluate_model(model, X, y) -> dict:
    """
    Evaluate a trained classification model and return standard metrics.

    This function is model-agnostic and can be used with any classifier
    that implements predict and predict_proba.
    """
    y_pred = model.predict(X)
    y_proba = model.predict_proba(X)[:, 1]

    return {
        "confusion_matrix": confusion_matrix(y, y_pred).tolist(),
        "classification_report": classification_report(
            y,
            y_pred,
            output_dict=True,
        ),
        "roc_auc": roc_auc_score(y, y_proba),
    }
