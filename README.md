# 📊 Customer Churn Prediction with ML & Automation

## 📌 Project Overview

This project focuses on building a predictive machine learning system to **identify customers at risk of churn**.

The goal is to predict whether a customer is likely to leave a service based on historical behavior and customer attributes.
The system is designed as an **end-to-end automated ML pipeline**, covering data ingestion, preprocessing, modeling, evaluation, and reporting.

---

## 🎯 Business Problem & Impact

Customer churn is a critical challenge for subscription-based and service-driven businesses, as acquiring new customers is often more expensive than retaining existing ones.

**This project helps businesses to:**

* Identify high-risk customers before they churn
* Take proactive retention actions
* Improve customer lifetime value
* Support data-driven decision-making

---

## 🧠 ML Approach
- Structured data ingestion & preprocessing
- Feature engineering using reusable modules
- Handling class imbalance in churn prediction
- Predictive modeling (classification)
- Model evaluation with reproducible metrics (ROC-AUC, Precision, Recall, F1)
- Explainability & business insight generation (SHAP)


*Models to be explored:*
- Random Forest
- Gradient Boosting

---

## 📁 Project Structure
```text
sales-churn-prediction/
│
├── data/
│   ├── raw/              → Original, immutable datasets
│   ├── processed/        → Cleaned & feature-engineered data
│   └── external/         → External data sources
│
├── notebooks/            → Exploratory analysis & experiments
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
│
├── src/                  → Production-ready Python code
│   ├── data/             → Data loading & preprocessing
│   ├── features/         → Feature engineering logic
│   ├── models/           → Training, evaluation & prediction
│   └── utils/            → Shared utilities & configuration
│
├── models/
│   ├── trained/          → Saved model artifacts
│   └── metrics/          → Model performance outputs
│
├── reports/
│   ├── figures/          → Generated plots
│   └── dashboards/       → Dashboards & reports
│
├── requirements.txt
├── .gitignore
├── CONTRIBUTING.md
└── README.md
```

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Power BI / Python Dashboards
* Git & GitHub

## ⚙️ Setup & Installation

### 🔹 Python Version

This project uses **Python 3.11**.
Make sure Python **3.11.x** is installed on your system before proceeding.

---

### 🔹 Clone the Repository

```bash
git clone https://github.com/IyadMahdy/churn-prediction.git
cd project-folder
```

---

### 🔹 Create a Virtual Environment

Create a virtual environment using Python 3.11:

```bash
py -3.11 -m venv venv
```

> Using a virtual environment is **strongly recommended** to isolate project dependencies.

---

### 🔹 Activate the Virtual Environment

**On Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

**On Linux / macOS:**

```bash
source venv/bin/activate
```

After activation, your terminal should show the virtual environment name.

---

### 🔹 Install Dependencies

Once the virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
- Jupyter notebooks are used for exploratory analysis and experimentation.
- Production-ready pipelines are implemented as modular Python scripts under `src/`.
- Trained models and metrics are saved for reuse and reporting.


Detailed usage instructions will be added as the project progresses.

---

## 📊 Results *(Coming Soon)*

Model performance metrics such as:

- ROC-AUC
- Precision / Recall
- F1-score

---

## 🤖 Automation & Reporting *(Coming Soon)*

* Automated prediction pipeline
* Scheduled reporting
* Business dashboards

---

## 👥 Contributors

* Iyad Mahdy – Team Lead
* Ahmed Abdulhakeem