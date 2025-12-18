# 📊 Customer Churn Prediction with ML & Automation

## 📌 Project Overview

This project focuses on building a predictive machine learning system to
**identify customers at risk of churn**.

The goal is to predict whether a customer is likely to leave a service based on
historical behavior and customer attributes. The system is designed as an
**end-to-end automated ML pipeline**, covering data ingestion, validation,
exploratory analysis, preprocessing, feature preparation, modeling, evaluation,
and reporting.

---

## 🎯 Business Problem & Impact

Customer churn is a critical challenge for subscription-based and
service-driven businesses, as acquiring new customers is often more expensive
than retaining existing ones.

**This project helps businesses to:**

- Identify high-risk customers before they churn
- Take proactive retention actions
- Improve customer lifetime value
- Support data-driven decision-making

---

## 📂 Dataset

This project uses the **IBM Telco Customer Churn** dataset.

- Problem type: Binary classification (customer churn prediction)
- Target variable: `Churn` (Yes / No)
- One row represents one customer
- Features include demographics, subscribed services, and billing information

Detailed dataset documentation can be found in `data/README.md`.

---

## 🧠 ML Approach

- Structured data ingestion with schema validation
- Exploratory Data Analysis (EDA) to inform preprocessing decisions
- Numeric data cleaning with preserved observations
- Categorical data inspection, validation, and encoding
- Feature engineering and feature selection (in progress)
- Handling class imbalance in churn prediction
- Baseline and advanced predictive modeling (classification)
- Model evaluation with reproducible metrics (ROC-AUC, Precision, Recall, F1)
- Explainability and business insight generation (planned)

_Models explored / planned:_

- Logistic Regression (baseline)
- Random Forest (baseline)
- Gradient Boosting

---

## 📁 Project Structure

```text
sales-churn-prediction/
│
├── data/
│   ├── raw/                    → Original, immutable datasets
│   ├── processed/              → Validated, cleaned & encoded data artifacts
│   └── external/               → External data sources
│
├── notebooks/                  → Exploratory analysis & validation
│   ├── 01_eda.ipynb
│   ├── 02_univariate_analysis.ipynb
│   ├── 03_correlation.ipynb
│   ├── 04_feature_target_analysis.ipynb
│   ├── 05_categorical_data_cleaning.ipynb
│   └── 06_duplicate_and_inconsistent_row_check.ipynb
│
├── src/                        → Production-ready Python code
│   ├── data/
│   │   ├── load_data.py        → Data ingestion & schema validation
│   │   ├── clean_numeric.py   → Numeric data cleaning
│   │   └── encode_categorical.py → Categorical feature encoding
│   ├── features/              → Feature engineering & selection logic
│   ├── models/                → Model training, evaluation & prediction
│   └── utils/
│       └── config.py           → Centralized paths & configuration
│
├── models/
│   ├── trained/               → Saved model artifacts
│   └── metrics/               → Model performance outputs
│
├── reports/
│   ├── figures/               → Generated plots
│   └── dashboards/            → Dashboards & reports
│
├── requirements.txt
├── .gitignore
├── CONTRIBUTING.md
└── README.md
```

---

## 🛠 Tech Stack

- Python 3.11.9
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Power BI / Python Dashboards
- Git & GitHub

---

## ⚙️ Setup & Installation

### 🔹 Python Version

This project uses **Python 3.11.9**.
Ensure Python **3.11.x** is installed before proceeding.

---

### 🔹 Clone the Repository

```bash
git clone https://github.com/IyadMahdy/churn-prediction.git
cd churn-prediction
```

---

### 🔹 Create a Virtual Environment

```bash
py -3.11 -m venv venv
```

> Using a virtual environment is **strongly recommended**.

---

### 🔹 Activate the Virtual Environment

**Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

---

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the pipeline steps in order:

- **Data ingestion & validation**

  ```bash
  python src/data/load_data.py
  ```

- **Numeric data cleaning**

  ```bash
  python src/data/clean_numeric.py
  ```

- **Categorical feature encoding**

  ```bash
  python src/data/encode_categorical.py
  ```

- Use Jupyter notebooks under `notebooks/` for exploratory analysis and data
  validation steps.

Further modeling and evaluation scripts are implemented under `src/models/`.

---

## 📊 Results _(In Progress)_

- Logistic Regression baseline metrics
- Random Forest baseline metrics
- Comparative evaluation (ROC-AUC, Precision, Recall, F1)

---

## 🤖 Automation & Reporting _(Planned)_

- Automated training and evaluation pipeline
- Reproducible experiment tracking
- Business-facing dashboards and reports

---

## 👥 Contributors

- **Iyad Mahdy** – Team Lead / Data Science
- **Ahmed Abdulhakeem** – Data Science
