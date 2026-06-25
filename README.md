# RetailMart Data Pipeline Project

## 📌 Project Overview

This project is a simple **Data Engineering pipeline** built for RetailMart Pvt. Ltd. It processes raw sales data from multiple CSV files, cleans and transforms it, and loads it into a SQLite database for analysis and reporting.

The goal is to convert messy real-world retail data into clean, structured, and insightful business data.

---

## ⚙️ Features

* Load multiple CSV files using Pandas
* Handle missing values and duplicate records
* Convert incorrect data types to proper formats
* Merge sales, product, and store data
* Create calculated field: **total_revenue**
* Perform data aggregation using Pandas and NumPy
* Store processed data into SQLite database
* Run SQL queries for business insights
* Generate summary reports (revenue, top products, top cities)
* Automated pipeline using a single function (`run_pipeline`)
* Basic error handling using try-except

---

## 🛠️ Tech Stack

* **Python** – Core programming language for data processing
* **Pandas** – Data cleaning, transformation, and analysis
* **NumPy** – Numerical computations and statistical analysis
* **SQLite** – Lightweight database for storing processed data
* **SQL** – Querying and generating business insights

---

## 📂 Project Structure

```
RetailMart_Project/
│
├── sales_data.csv
├── products.csv
├── stores.csv
├── retail_pipeline.py
├── retailmart.db
└── Project_Documentation.docx
```

---

## 🔄 Workflow

1. Load CSV files (Sales, Products, Stores)
2. Data cleaning (remove duplicates, handle missing values)
3. Data transformation (merge datasets, create new columns)
4. Load cleaned data into SQLite database
5. Run SQL queries for insights
6. Generate summary report
7. Execute full pipeline using `run_pipeline()`

---

## 📊 Key Insights Generated

* Total revenue of the business
* Top-selling products
* Top-performing cities
* Revenue per store per day
* Transaction-level analysis

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/retailmart-data-pipeline.git
```

2. Install required libraries:

```bash
pip install pandas numpy
```

3. Run the script:

```bash
python retail_pipeline.py
```

---

## 🚀 Future Improvements

* Add real-time data ingestion
* Use PostgreSQL instead of SQLite
* Build dashboard using Power BI / Tableau
* Automate pipeline using Apache Airflow
* Add logging system for better tracking

---

## 👨‍💻 Author

Created as a Data Engineering learning project to demonstrate ETL pipeline development using Python.

---

⭐ If you like this project, feel free to star the repository!
