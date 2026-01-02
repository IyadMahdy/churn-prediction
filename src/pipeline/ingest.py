from src.data.load_data import ingest_data


def run_ingestion():
    """
    End-to-end ingestion pipeline:
    - Load raw data
    - Validate schema
    - Persist validated dataset
    """
    return ingest_data(
        filename="telco_customer_churn.csv",
        processed_filename="telco_customer_churn_validated.csv",
    )


if __name__ == "__main__":
    df = run_ingestion()
    print("Ingestion pipeline completed. Shape:", df.shape)
