import pandas as pd
'''

Creating data

Selecting data

Filtering data

Cleaning data

Transforming columns

Aggregating data

Merging datasets

Exporting results
'''

#Cretaing data frame using dictionary
data = {
    "Name": ["Ram", "Sam", "John", "Priya"],
    "Age": [25, 30, 28, 22],
    "Salary": [40000, 50000, 45000, 30000]
}
df = pd.DataFrame(data)
print(df)

#selecting single data
print(df["Age"])

#selecting multiple data
print(df[["Age", "Name"]])

#select rows using iloc and loc
print(df.loc[0:2]) # nth index
print(df.iloc[0:1]) # n-1 index

#filtering based on the conditions
df = pd.DataFrame(data)
print(df)

#employee with salary > 40000
filtered = df[df["Salary"] > 40000]
print(filtered)
filtered = df[df["Salary"] <= 40000]
print(filtered)
#multiple conditions
filtered = df[(df["Salary"] > 40000) & (df["Age"] > 25)]
print(filtered)

#adding or modifying the columns
data = {
    "Name": ["Ram", "Sam", "John", "Priya"],
    "Salary": [40000, 50000, 45000, 30000]
}

df = pd.DataFrame(data)
#add the bonus column
df["Bonus"] = df["Salary"]*0.10
print(df)
#modify the current column - increase the columns
df["Salary"] = df["Salary"] + 2000
print(df)

# Sorting in ascending or descending order
data = {
    "Name": ["Ram", "Sam", "John", "Priya"],
    "Age": [25, 30, 28, 22],
    "Salary": [40000, 50000, 45000, 30000]
}
df = pd.DataFrame(data)
#sort the salary in ascending order
sorted_df = df.sort_values(by=["Salary"], ascending=True)
print(sorted_df)
#sort the salary in descending order
sorted_df = df.sort_values(by=["Salary"], ascending=False)
print(sorted_df)

#handling missing value
import numpy as np
#replace the all the missing values (NaN) in the DataFrame with 0
data = {
    "Name": ["Ram", "Sam", None],
    "Age": [25, np.nan, 30]
}

df = pd.DataFrame(data)
print("missing values")
print(df.isnull())

#fill the missing values - replace all the missing values (NaN, None, NaT) in the DataFrame with 0
df_filled = df.fillna(0)
print(df_filled)

data = {
    "Age": [25, None, 30],
    "Salary": [50000, 60000, None]
}
df = pd.DataFrame(data)
print(df)

df = df.fillna(0)
print(df)

#drop missing rows
data = {
    "Name": ["A", "B", "C"],
    "Age": [25, None, 30],
    "Salary": [50000, 60000, None]
}
df = pd.DataFrame(data)
print(df)

df_dropped = df.dropna()
print(df_dropped)

#GroupBy and Aggregation
data = {
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai"],
    "Salary": [40000, 50000, 45000, 30000]
}
df = pd.DataFrame(data)

#average salary per city
result = df.groupby("City")["Salary"].mean()
print(result)

#Multiple Aggregation
result = df.groupby("City")["Salary"].agg(["mean", "sum", "count"])
print(result)

#Merging DataFrames
df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Ram", "Sam"]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Salary": [40000, 50000]
})

merged = pd.merge(df1, df2, on="ID", how ="inner")
print(merged)

#removing Duplicates
data = {
    "Name": ["Ram", "Sam", "Ram"],
    "Salary": [40000, 50000, 40000],
}
df = pd.DataFrame(data)
print("Before removing duplicates:")
print(df)
df = df.drop_duplicates()
print("After removing duplicates:")
print(df)


