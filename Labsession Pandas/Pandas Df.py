import pandas as pd
import numpy as np
#Create a DataFrame containing missing values
data = {
    "Name": ["Ravi", "Anjali", "Rahul", "Priya", "Kiran"],
    "Age": [25, np.nan, 30, 22, np.nan],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, np.nan, 45000, 55000],
    "City": ["Bangalore", "Delhi", "Bangalore", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)
print("Original DataFrame", df)

#Detect missing values
print("Missing value")
print(df.isnull())

#Replace missing values with 0
df_filled = df.fillna(0)
print("After replacing missing values with 0", df_filled)

#Drop rows containing missing values
df_dropped = df.dropna()
print("After dropping rows with missing values", df_dropped)

#Sort DataFrame by Age (ascending)
sorted_age = df.sort_values(by="Age", ascending=True)
print("Sorted by Age (ascending)", sorted_age)

#Sort DataFrame by Salary (descending)
sorted_salary = df.sort_values(by="Salary", ascending=False)
print("Sorted by Salary (descending)", sorted_salary)

#Groupby Department → Average Salary
avg_salary = df.groupby("Department")["Salary"].mean()
print("Average Salary per Department", avg_salary)

#Total Salary per Department
total_salary = df.groupby("Department")["Salary"].sum()
print("Total Salary per Department", total_salary)

#Filter employees where Age > 25 AND City = "Bangalore"
filtered = df[(df["Age"] > 25) & (df["City"] == "Bangalore")]
print("Filtered Employees", filtered)

#Create new column "Tax" (10% of Salary using apply())
df["Tax"] = df["Salary"].apply(lambda x: x * 0.10 if pd.notnull(x) else x)
print("DataFrame with Tax column", df)
