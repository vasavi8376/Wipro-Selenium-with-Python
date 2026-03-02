import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = {
    "Day": ["Mon","Tue","Wed","Thur","Fri"],
    "Steps": [4000,5500,7000,6500,8000]
}

df = pd.DataFrame(data)
df.plot(x ="Day",y ="Steps",kind = "bar")
plt.title("Daily Steps count")
plt.xlabel("Day")
plt.ylabel("Steps")
#save as image - jpg
plt.savefig("Barchart.jpg")

#save as PDF
plt.savefig("bar.pdf", format="pdf")