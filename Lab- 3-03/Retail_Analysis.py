import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df = pd.read_csv("retail_data.csv")

#step - 1 Data Cleaning
#convert date to datetime
df['Date'] = pd.to_datetime(df['Date'])
#creating a new column
df['Revenue'] = df['Quantity'] * df['Price']
#check for null values
print("Null Values", df.isnull().sum())
#handling the null values
df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(0)
df['Region'] = df['Region'].fillna("Unknown")
df['Category'] = df['Category'].fillna("Unknown")
df['Product'] = df['Product'].fillna("Unknown")

#step - 2 Data Analysis
#region with the highest total revenue
region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
print("Revenue by Region:", region_revenue)
print("Highest Revenue Region:", region_revenue.idxmax())
#monthly sales trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Revenue'].sum()
print("Monthly Revenue:", monthly_revenue)
# the best perform category
category_revenue = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print("Best Performing Category:", category_revenue.idxmax())
#the top 5 products by revenue
top5_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(5)
print("Top 5 Products:", top5_products)

#step 3 visualizations
#bar chart - Revenue by Region
plt.figure()
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.show()
#line plot - Monthly Revenue Trend
plt.figure()
monthly_revenue.plot(kind="line")
plt.title("Monthly Revenue Trend")
plt.xticks(rotation=45)
plt.show()
#pie chart - Category Contribution
plt.figure()
category_revenue.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Contribution")
plt.ylabel("")
plt.show()
#horizontal bar chart - Top 5 Products
plt.figure()
top5_products.plot(kind="barh")
plt.title("Top 5 Products")
plt.gca().invert_yaxis()
plt.show()
