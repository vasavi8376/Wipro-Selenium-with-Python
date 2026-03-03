import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read csv file
df = pd.read_csv("student_data.csv")

#step 1 - Feature Engineering
#Average Marks
df["Average_Marks"] = df[["Math", "Science", "English"]].mean(axis=1)
#Result Column
df["Result"] = df["Average_Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

#step2 - Analysis
# the average score per subject
subject_avg = df[["Math","Science","English"]].mean()
print("Average per Subject:", subject_avg)
# attendance correlate with performance
correlation = df["Attendance"].corr(df["Average_Marks"])
print("Attendance vs Performance Correlation:", correlation)
# Compare performance by gender
gender_performance = df.groupby("Gender")["Average_Marks"].mean()
print("Performance by Gender:", gender_performance)
# students passed vs failed
result_count = df["Result"].value_counts()
print("Pass vs Fail:", result_count)


#step3 - Visualizations
#Bar chart - Average subject scores
plt.figure()
subject_avg.plot(kind="bar")
plt.title("Average Subject Scores")
plt.ylabel("Average Marks")
plt.show()
#Scatter plot - Attendance vs Average Marks
plt.figure()
plt.scatter(df["Attendance"], df["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()
#Boxplot - Marks distribution by Gender
df.boxplot(column="Average_Marks", by="Gender")
plt.title("Marks Distribution by Gender")
plt.suptitle("")
plt.show()
#Pie chart - Pass vs Fail
plt.figure()
result_count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.ylabel("")
plt.show()