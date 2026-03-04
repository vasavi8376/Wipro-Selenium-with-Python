import pandas as pd
from openpyxl import load_workbook

#writing to excel
data = {
    "Name": ["Ram", "Ravi", "Sita"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

df.to_excel("output.xlsx", index=False, engine="openpyxl")
#read specific column
df = pd.read_excel("output.xlsx", usecols=["Name"], engine="openpyxl")
print(df)

# Read particular sheet
df = pd.read_excel("output.xlsx", sheet_name="Sheet1", engine="openpyxl")
print(df)

#  Read ALL sheets from Excel
df = pd.read_excel("student.xlsx", sheet_name=None)
print(df)

# Writing MULTIPLE sheets to Excel
data1 = {
    "Product": ["Laptop", "Phone"],
    "Sales": [10, 20]
}

data2 = {
    "City": ["Delhi", "Mumbai"],
    "Customers": [200, 150]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

with pd.ExcelWriter("report.xlsx", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Sales")
    df2.to_excel(writer, sheet_name="Customers")