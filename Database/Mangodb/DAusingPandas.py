import pandas as pd
from CRUD import collection
from pymongo import MongoClient

data = list(collection.find())
df = pd.DataFrame(data)
print(df)

print(df["marks"].mean())

print(df["marks"] == df["marks"].max())

print(df.groupby("subject")["marks"].mean())
