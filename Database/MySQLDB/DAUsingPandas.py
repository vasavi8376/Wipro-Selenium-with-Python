import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:Lalitha%40123@localhost/school")

df = pd.read_sql("select * from students", engine)
print(df)

#average marks
print(df["marks"].mean())

#highest score
print(df[df["marks"] == df["marks"].max()])

#group by subject
print(df.groupby('subject')["marks"].mean())
