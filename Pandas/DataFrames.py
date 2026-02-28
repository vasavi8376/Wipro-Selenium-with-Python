#data frame is a 2 dimensional labeled data structure (rows and columns
#like an Excel SQL Tables
import pandas as pd

#create dataframe from list of dictionaries

data = [
    {"Name": "Ram", "Age": 25},
    {"Name": "Sam", "Age": 30},
    {"Name": "John", "Age": 28},
]

df = pd.DataFrame(data)
print(df)

#create dataframe from Dictionary of series
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

df = pd.DataFrame({"A": s1,"B":s2})
print(df)

#create Dataframe from numpy array
import numpy as np

arr = np.array([[1,2], [3,4], [5,6]])
df = pd.DataFrame(arr, columns=["A","B"])
print(df)

#create data frame using csv file
df = pd.read_csv("employee.csv")
print(df)

#create empty df
df = pd.DataFrame()
print(df)

#create DataFrame with Custom Index

data = {
    "Name": ["Ram", "Sam"],
    "Age": [25, 30] }
df = pd.DataFrame(data, index = ["Emp1", "Emp2"])
print(df)