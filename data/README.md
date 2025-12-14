## 📊 Dataset Documentation – Telco Customer Churn (IBM)

## 📌 Context

This dataset is provided by **IBM Sample Data Sets** and is designed to support customer retention analysis.

> **Objective:**
> Predict customer behavior to retain customers by analyzing relevant customer data and developing focused customer retention programs.

---

## 🧾 Dataset Description

Each row in the dataset represents **a single customer**, and each column corresponds to a specific **customer attribute**.

The dataset includes information about:

* Customers who left within the last month (**Churn**)
* Services each customer has signed up for
* Customer account and billing information
* Customer demographic characteristics

---

## 🎯 Problem Definition

* **Task:** Predict whether a customer will churn
* **Problem Type:** Binary Classification
* **Target Variable:** `Churn`
* **Granularity:** One row per customer

---

## 🎯 Target Variable

| Column | Type                 | Description                                                 | Expected Values |
| ------ | -------------------- | ----------------------------------------------------------- | --------------- |
| Churn  | Categorical (Binary) | Whether the customer left the company within the last month | Yes, No         |

---

## 🧍 Customer Demographics

| Column        | Type         | Description                              | Expected Values |
| ------------- | ------------ | ---------------------------------------- | --------------- |
| customerID    | String       | Unique customer identifier               | Unique ID       |
| gender        | Categorical  | Customer gender                          | Male, Female    |
| SeniorCitizen | Binary (int) | Whether the customer is a senior citizen | 1 = Yes, 0 = No |
| Partner       | Categorical  | Whether the customer has a partner       | Yes, No         |
| Dependents    | Categorical  | Whether the customer has dependents      | Yes, No         |

---

## ⏳ Customer Account Information

| Column           | Type        | Description                                               | Expected Values                                                                    |
| ---------------- | ----------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| tenure           | Integer     | Number of months the customer has stayed with the company | ≥ 0                                                                                |
| Contract         | Categorical | Contract duration                                         | Month-to-month, One year, Two year                                                 |
| PaperlessBilling | Categorical | Whether the customer uses paperless billing               | Yes, No                                                                            |
| PaymentMethod    | Categorical | Customer’s payment method                                 | Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic) |

---

## 📞 Phone Services

| Column        | Type        | Description                                   | Expected Values           |
| ------------- | ----------- | --------------------------------------------- | ------------------------- |
| PhoneService  | Categorical | Whether the customer has phone service        | Yes, No                   |
| MultipleLines | Categorical | Whether the customer has multiple phone lines | Yes, No, No phone service |

---

## 🌐 Internet & Additional Services

| Column           | Type        | Description              | Expected Values              |
| ---------------- | ----------- | ------------------------ | ---------------------------- |
| InternetService  | Categorical | Type of internet service | DSL, Fiber optic, No         |
| OnlineSecurity   | Categorical | Online security add-on   | Yes, No, No internet service |
| OnlineBackup     | Categorical | Online backup add-on     | Yes, No, No internet service |
| DeviceProtection | Categorical | Device protection add-on | Yes, No, No internet service |
| TechSupport      | Categorical | Technical support add-on | Yes, No, No internet service |
| StreamingTV      | Categorical | Streaming TV service     | Yes, No, No internet service |
| StreamingMovies  | Categorical | Streaming movies service | Yes, No, No internet service |

---

## 💰 Billing Information

| Column         | Type  | Description                            | Expected Values |
| -------------- | ----- | -------------------------------------- | --------------- |
| MonthlyCharges | Float | Monthly amount charged to the customer | ≥ 0             |
| TotalCharges   | Float | Total amount charged to the customer   | ≥ 0             |

---

## ⚠️ Important Notes & Assumptions

* `customerID` is an identifier and **should not be used as a predictive feature**.
* `SeniorCitizen` is encoded numerically (0/1) instead of categorical values.
* Service-related features include **"No internet service"**, which represents a valid category and not missing data.
* `TotalCharges` may require **type conversion** during preprocessing.
* Class imbalance in `Churn` is expected and will be explored during EDA.
* Detailed data quality checks (missing values, distributions, outliers) are performed during **EDA**, not during ingestion.

---

## 💡 Inspiration & Use Case

This dataset is commonly used to:

* Explore customer churn behavior
* Build and evaluate churn prediction models
* Learn customer retention strategies and feature importance

---

## ✅ Dataset Readiness

* Required columns are validated during data ingestion.
* Dataset is suitable for exploratory data analysis, feature engineering, and machine learning modeling.