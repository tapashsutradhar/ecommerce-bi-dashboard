# E-commerce BI Dashboard

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-green?logo=streamlit)]
[![SQL](https://img.shields.io/badge/SQL-MySQL-orange?logo=mysql)]
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🔹 Project Overview

The **E-commerce BI Dashboard** is a complete end-to-end project designed to analyze e-commerce business performance using SQL, Python, and interactive dashboards. It provides actionable insights for **sales trends, customer segmentation, product performance, and revenue forecasting**.

This project is ideal for **business analysts, data analysts, or data scientists** to demonstrate **business intelligence and analytics skills**.

---

## 🔹 Features

- **Sales Analytics**
  - Total revenue, total orders, and units sold
  - Monthly and quarterly sales trends
  - Top products by units sold and revenue

- **Customer Analytics**
  - RFM (Recency, Frequency, Monetary) segmentation
  - Top customers and loyalty analysis

- **Product Analytics**
  - Best-selling products and categories
  - Inventory trends

- **Forecasting**
  - Predict future sales using time-series models (Holt-Winters / ARIMA)

- **Dashboards**
  - Interactive visualizations with **Streamlit**, **Power BI**, and **Tableau**

---

## 🔹 Repository Structure
```
ecommerce-bi-dashboard/
├── data/
│ ├── raw/ # Original CSV files
│ └── processed/ # Cleaned dataset
├── sql/ # SQL scripts (schema, cleaning, analysis)
├── notebooks/ # Jupyter notebooks (EDA, cleaning, forecasting)
├── src/ # Python scripts for data loading, preprocessing, visualization, modeling
├── dashboard/ # Streamlit / Power BI / Tableau dashboards
├── reports/ # PDF reports / analysis summaries
├── requirements.txt
└── README.md
```


---

## 🔹 Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/tapashsutradhar/ecommerce-bi-dashboard.git
cd ecommerce-bi-dashboard
```

2. **Install Python dependencies**

```bash
pip install -r requirements.txt
```

3. **Run Streamlit Dashboard**

```bash
streamlit run dashboard/streamlit_app.py
```

4. Open Power BI or Tableau dashboards located in the `dashboard/` folder.

---

## 🔹 Sample CSV Dataset Structure

**customers.csv**

| CustomerID | FirstName | LastName | Email | City | Country | JoinDate |
| ---------- | --------- | -------- | ----- | ---- | ------- | -------- |

**products.csv**

| ProductID | ProductName | Category | Price |

**orders.csv**

| OrderID | CustomerID | ProductID | Quantity | OrderDate | TotalAmount |

---

## 🔹 Tags / Topics

`ecommerce` `business-intelligence` `BI-dashboard` `python` `sql` `streamlit` `powerbi` `tableau` `data-analysis` `forecasting` `EDA` `customer-segmentation` `product-analytics` `time-series`

---

## 🔹 Screenshots / Preview

> screenshots of Streamlit dashboard, Power BI visuals, and plots from notebooks here for better visual appeal.

---

## 🔹 Connect

* GitHub: [tapashsutradhar](https://github.com/tapashsutradhar)
* LinkedIn: [linkedin.com/in/tapashsutradhar](https://linkedin.com/in/tapashsutradhar)

---

## 🔹 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
