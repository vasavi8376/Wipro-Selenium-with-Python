import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# CONNECT TO MYSQL SERVER
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lalitha@123",
)
cursor = connection.cursor()
print("Connected Successfully")

# CREATE DATABASE
cursor.execute("CREATE DATABASE IF NOT EXISTS retail")
connection.commit()

# RECONNECT TO DATABASE
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lalitha@123",
    database="retail"
)
cursor = connection.cursor()
print("Connected to 'retail' database successfully")

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    orderid INT AUTO_INCREMENT PRIMARY KEY,
    orderdate DATE,
    region VARCHAR(50),
    product VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price FLOAT
)
""")
connection.commit()

# CLEAR OLD DATA (Important)
cursor.execute("DELETE FROM sales")
connection.commit()

# INSERT DATA (Correct Format)
query = """
INSERT INTO sales(orderdate, region, product, category, quantity, price)
VALUES (%s,%s,%s,%s,%s,%s)
"""

sales_data = [
    ('2024-01-05','East','Laptop','Electronics',2,50000),
    ('2024-01-08','West','Shirt','Clothing',5,1500),
    ('2024-01-12','North','Table','Furniture',1,8000),
    ('2024-02-02','South','Mobile','Electronics',3,20000),
    ('2024-02-10','East','Shoes','Clothing',4,2500)
]

cursor.executemany(query, sales_data)
connection.commit()
print("Data Inserted Successfully")


# READ DATA INTO PANDAS
cursor.execute("SELECT * FROM sales")
rows = cursor.fetchall()

columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(rows, columns=columns)

print("Data from MySQL:")
print(df)


# DATA CLEANING
df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")

# Create Revenue Column
df["Revenue"] = df["quantity"] * df["price"]

# Check Null Values
print("Null Values:")
print(df.isnull().sum())

df.fillna(0, inplace=True)


# ANALYSIS

# Revenue by Region
region_revenue = df.groupby("region")["Revenue"].sum()
print("Revenue by Region:")
print(region_revenue)
print("Highest Revenue Region:", region_revenue.idxmax())

# Monthly Revenue
df["Month"] = df["orderdate"].dt.to_period("M")
monthly_revenue = df.groupby("Month")["Revenue"].sum()
print("Monthly Revenue:")
print(monthly_revenue)

# Category Performance
category_revenue = df.groupby("category")["Revenue"].sum()
print("Category Revenue:")
print(category_revenue)
print("Best Category:", category_revenue.idxmax())

# Top 5 Products
top_products = (
    df.groupby("product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print("Top 5 Products:")
print(top_products)

# VISUALIZATIONS

plt.figure()
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.show()

plt.figure()
monthly_revenue.plot()
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue")
plt.show()

plt.figure()
category_revenue.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Contribution")
plt.ylabel("")
plt.show()

plt.figure()
top_products.plot(kind="barh")
plt.title("Top 5 Products")
plt.xlabel("Revenue")
plt.show()

# UPDATE EXAMPLE
cursor.execute("UPDATE sales SET price=55000 WHERE product='Laptop'")
connection.commit()

# DELETE EXAMPLE
cursor.execute("DELETE FROM sales WHERE product='Shoes'")
connection.commit()

print("Update and Delete operations completed successfully")

# CLOSE CONNECTION
cursor.close()
connection.close()
print("Connection Closed Successfully")