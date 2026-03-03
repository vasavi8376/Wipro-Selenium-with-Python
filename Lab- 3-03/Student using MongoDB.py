# MongoDB Connection
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

client = MongoClient("mongodb://localhost:27017/")
print("Connected successfully")

# Create Database and Collection
db = client["school"]
collection = db["students"]

# Clear old data (optional)
collection.delete_many({})

# Insert Your Given Data
students = [
    {"StudentID": 1, "Gender": "Male", "Math": 80, "Science": 75, "English": 78, "Attendance": 90},
    {"StudentID": 2, "Gender": "Female", "Math": 35, "Science": 40, "English": 38, "Attendance": 60},
    {"StudentID": 3, "Gender": "Male", "Math": 60, "Science": 55, "English": 58, "Attendance": 75},
    {"StudentID": 4, "Gender": "Female", "Math": 45, "Science": 50, "English": 48, "Attendance": 70},
    {"StudentID": 5, "Gender": "Male", "Math": 30, "Science": 35, "English": 32, "Attendance": 50}
]

collection.insert_many(students)
print("Data Inserted Successfully")

# Print All Data
for doc in collection.find():
    print(doc)


# Convert MongoDB Data to Pandas

data = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(data)


# Average marks
df["Average_Marks"] = df[["Math", "Science", "English"]].mean(axis=1)

df["Result"] = df["Average_Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("Data with Calculated Columns:")
print(df)

# Average score per subject
subject_avg = df[["Math", "Science", "English"]].mean()

# Correlation between Attendance & Performance
correlation = df["Attendance"].corr(df["Average_Marks"])

# Performance by Gender
gender_performance = df.groupby("Gender")["Average_Marks"].mean()

# Pass vs Fail count
result_counts = df["Result"].value_counts()

print("Average Score Per Subject:", subject_avg)
print("Attendance vs Average Marks Correlation:", correlation)
print("Performance by Gender:", gender_performance)
print("Pass vs Fail:", result_counts)


# Update
collection.update_one(
    {"StudentID": 5},
    {"$set": {"Math": 45}}
)


# Delete
collection.delete_one({"StudentID": 2})

print("Update and Delete operations completed successfully")

# Bar Chart → Average Subject Scores
plt.figure()
subject_avg.plot(kind="bar")
plt.title("Average Subject Scores")
plt.ylabel("Marks")
plt.show()

# Scatter Plot → Attendance vs Average Marks
plt.figure()
plt.scatter(df["Attendance"], df["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()

# Boxplot → Marks by Gender
plt.figure()
df.boxplot(column="Average_Marks", by="Gender")
plt.title("Marks Distribution by Gender")
plt.suptitle("")
plt.ylabel("Average Marks")
plt.show()

# Pie Chart → Pass vs Fail
plt.figure()
result_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail Distribution")
plt.ylabel("")
plt.show()