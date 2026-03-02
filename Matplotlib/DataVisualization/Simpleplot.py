import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x,y)

#x-axis
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple plot')

#show method will display the data

plt.show()

#simple data
subjects = ["Maths", "Science", "English", "History", "Computer"]
marks = [85, 78, 92, 74, 88]

#create the line graph
plt.plot(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()


#matplotlib with pandas integration
data = {
    "Month":["jan","feb","mar","apr","may"],
    "Sales":[100, 150, 130, 170, 160]
}

df = pd.DataFrame(data)

plt.plot(df["Month"],df["Sales"])

#x axis plot
plt.title("Monthly sales")
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()