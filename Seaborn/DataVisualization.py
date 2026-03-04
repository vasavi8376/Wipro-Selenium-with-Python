import seaborn as sns
import matplotlib.pyplot as plt

#basic plot(line plot)
#load the sample data set
data = sns.load_dataset("flights")
#line plot
sns.lineplot(x = "year", y = "passengers", data = data)
plt.title("yearly passenger growth")
plt.show()

#bar plot
data = sns.load_dataset("tips")
sns.barplot(x= "day", y= "total_bill", data= data)
plt.title("Average bill per day")
plt.show()

#scatter plot
data = sns.load_dataset("tips")
sns.scatterplot(x= "total_bill", y= "tip", data= data)
plt.title("Total bill vs tip")
plt.show()

#histogram
data = sns.load_dataset("tips")
sns.histplot(data["total_bill"], bins= 20)
plt.title("Total bill vs tip")
plt.show()

#Box plot
data = sns.load_dataset("tips")
sns.boxplot(x= "day", y= "total_bill", data= data)
plt.title("Bill distribution by day")
plt.show()

#heat map
data = sns.load_dataset("tips")
cor1 = data.corr(numeric_only = True)
sns.heatmap(cor1, annot = True, cmap = "coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#Pair plots
data = sns.load_dataset("iris")
sns.pairplot(data)
plt.show()

#voilin plot
data = sns.load_dataset("tips")
sns.violinplot(x= "day", y= "total_bill", data= data)
plt.title("Bill distribution by day")
plt.show()

#count plot
data = sns.load_dataset("tips")
sns.countplot(x= "day", data= data)
plt.title("Numbers of customers per day")
plt.show()

#regression plot
data = sns.load_dataset("tips")
sns.regplot(x= "total_bill", y= "tip", data= data)
plt.title("Regression between bill and tip")
plt.show()