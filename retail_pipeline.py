import pandas as pd
import numpy as np
import sqlite3

# task-1
# Load CSV files
sales_df = pd.read_csv("sales_data.csv")
products_df = pd.read_csv("products.csv")
stores_df = pd.read_csv("stores.csv")

print("Files loaded successfully!")

#shape and first 5 rows of each
print("Sales Data Shape:", sales_df.shape)
print(sales_df.head())

print("\nProducts Data Shape:", products_df.shape)
print(products_df.head())

print("\nStores Data Shape:", stores_df.shape)
print(stores_df.head())

# Check missing values and summary of columns having missing values

print("\nSales Data Missing Values:")
print(sales_df.isnull().sum())

print("\nProducts Data Missing Values:")
print(products_df.isnull().sum())

print("\nStores Data Missing Values:")
print(stores_df.isnull().sum())

#task-2
# Count duplicate rows
duplicate_count = sales_df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)

# Remove duplicates
sales_df = sales_df.drop_duplicates()

print("Shape after removing duplicates:", sales_df.shape)

# Fill missing quantity values with 0
sales_df['quantity'] = sales_df['quantity'].fillna(0)

# Remove rows where amount is NULL
sales_df = sales_df.dropna(subset=['amount'])

# Check new shape
print("Shape after cleaning:", sales_df.shape)

# Convert sale_date to datetime
sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])

# Convert amount to float
sales_df['amount'] = sales_df['amount'].astype(float)

#task-3
#merge all dataframe

merged_df = pd.merge(
    sales_df,
    products_df,
    on='product_id',
    how='left'
)

merged_df = pd.merge(
    merged_df,
    stores_df,
    on='store_id',
    how='left'
)

# merged dataframe
print("Merged Data Shape:", merged_df.shape)
print(merged_df.head())

# create column total_revenue

merged_df['total_revenue'] = merged_df['quantity'] * merged_df['price']

# mean, max and min of total revenue

print("Mean Revenue:", np.mean(merged_df['total_revenue']))
print("Maximum Revenue:", np.max(merged_df['total_revenue']))
print("Minimum Revenue:", np.min(merged_df['total_revenue']))

# total revenue generated per city

city_revenue = (
    merged_df.groupby('city')['total_revenue']
    .sum()
    .sort_values(ascending=False)
)
print("Total revenue generated per city")
print(city_revenue)

#task-4
# SQLite database

conn = sqlite3.connect("retailmart.db")

merged_df.to_sql(
    "retail_sales",
    conn,
    if_exists="replace",
    index=False
)

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM retail_sales")

print("Rows in retail_sales table:", cursor.fetchone()[0])

conn.close()

#  SQL query to find the Top 3 best-selling products


conn = sqlite3.connect("retailmart.db")

query = """
SELECT
    product_name,
    SUM(quantity) AS total_quantity_sold
FROM retail_sales
GROUP BY product_name
ORDER BY total_quantity_sold DESC
LIMIT 3;
"""

result = conn.execute(query)

for row in result:
    print(row)

conn.close()

#task-5
#SQL query to find total revenue per store per day 

conn = sqlite3.connect("retailmart.db")

query = """
SELECT
    store_name,
    sale_date,
    SUM(total_revenue) AS total_revenue
FROM retail_sales
GROUP BY store_name, sale_date
ORDER BY sale_date, total_revenue DESC;
"""

result = conn.execute(query)

for row in result:
    print(row)

conn.close()

# summary report

# Total number of transactions
total_transactions = len(merged_df)

# Total revenue
total_revenue = merged_df['total_revenue'].sum()

# Top selling city
top_city = city_revenue.idxmax()

# Top selling product
top_product = (
    merged_df.groupby('product_name')['quantity']
    .sum()
    .idxmax()
)

print("\n===== SUMMARY REPORT =====")
print("Total Transactions :", total_transactions)
print("Total Revenue      :", total_revenue)
print("Top Selling City   :", top_city)
print("Top Selling Product:", top_product)

#task-6
#run_pipeline() that runs all the above steps and handle basic errors

def run_pipeline():
    try:
        # Load files
        sales_df = pd.read_csv("sales_data.csv")
        products_df = pd.read_csv("products.csv")
        stores_df = pd.read_csv("stores.csv")

        print("Files loaded successfully!")

        # Remove duplicates
        sales_df = sales_df.drop_duplicates()

        # Handle missing values
        sales_df['quantity'] = sales_df['quantity'].fillna(0)
        sales_df = sales_df.dropna(subset=['amount'])

        # Convert datatypes
        sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])
        sales_df['amount'] = sales_df['amount'].astype(float)

        # Merge data
        merged_df = pd.merge(
            sales_df,
            products_df,
            on='product_id',
            how='left'
        )

        merged_df = pd.merge(
            merged_df,
            stores_df,
            on='store_id',
            how='left'
        )

        # Create revenue column
        merged_df['total_revenue'] = (
            merged_df['quantity'] * merged_df['price']
        )

        # Revenue by city
        city_revenue = (
            merged_df.groupby('city')['total_revenue']
            .sum()
            .sort_values(ascending=False)
        )

        # Load into SQLite
        conn = sqlite3.connect("retailmart.db")

        merged_df.to_sql(
            "retail_sales",
            conn,
            if_exists="replace",
            index=False
        )

        conn.close()

        # Summary Report
        total_transactions = len(merged_df)
        total_revenue = merged_df['total_revenue'].sum()

        top_city = city_revenue.idxmax()

        top_product = (
            merged_df.groupby('product_name')['quantity']
            .sum()
            .idxmax()
        )

        print("\n===== SUMMARY REPORT =====")
        print("Total Transactions :", total_transactions)
        print("Total Revenue      :", total_revenue)
        print("Top Selling City   :", top_city)
        print("Top Selling Product:", top_product)

        print("\nPipeline executed successfully!")

    except FileNotFoundError as e:
        print("File not found:", e)

    except Exception as e:
        print("An error occurred:", e)
run_pipeline()