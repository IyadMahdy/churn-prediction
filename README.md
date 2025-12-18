# 📊 Customer Churn Prediction with ML & Automation

## 📌 Project Overview

This project focuses on building a predictive machine learning system to
**identify customers at risk of churn**.

The goal is to predict whether a customer is likely to leave a service based on
historical behavior and customer attributes. The system is designed as an
**end-to-end automated ML pipeline**, covering data ingestion, validation,
exploratory analysis, preprocessing, modeling, evaluation, and reporting.

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
- Robust numeric and categorical data cleaning
- Feature engineering using reusable modules
- Handling class imbalance in churn prediction
- Predictive modeling (classification)
- Model evaluation with reproducible metrics (ROC-AUC, Precision, Recall, F1)
- Explainability and business insight generation (SHAP)

_Models to be explored:_

- Logistic Regression (baseline)
- Random Forest
- Gradient Boosting

---

## 📁 Project Structure

```text
sales-churn-prediction/
│
├── data/
│   ├── raw/                    → Original, immutable datasets
│   ├── processed/              → Validated & cleaned data artifacts
│   └── external/               → External data sources
│
├── notebooks/                  → Exploratory analysis
│   ├── 01_eda.ipynb
│   ├── 02_univariate_analysis.ipynb
│   ├── 03_correlation.ipynb
│   └── 04_feature_target_analysis.ipynb
│
├── src/                        → Production-ready Python code
│   ├── data/
│   │   ├── load_data.py        → Data ingestion & validation
│   │   └── clean_numeric.py   → Numeric data cleaning
│   ├── features/              → Feature engineering logic
│   ├── models/                → Training, evaluation & prediction
│   └── utils/                 → Shared utilities & configuration
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

- Run data ingestion and validation:

  ```bash
  python src/data/load_data.py
  ```

- Run numeric data cleaning:

  ```bash
  python src/data/clean_numeric.py
  ```

- Use Jupyter notebooks for exploratory analysis.

- Production-ready pipelines are implemented under `src/`.

More detailed usage instructions will be added as the project progresses.

---

## 📊 Results _(Coming Soon)_

- ROC-AUC
- Precision
- Recall
- F1-score

---

## 🤖 Automation & Reporting _(Coming Soon)_

- Automated prediction pipeline
- Scheduled reporting
- Business dashboards

---

## 👥 Contributors

- Iyad Mahdy – Team Lead
- Ahmed Abdulhakeem
