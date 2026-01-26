import pandas as pd
df = pd.read_csv("students.txt",header=None,names=["roll","name","marks"])
print("maximum marks:",df["marks"].max())
print("minimum marks:",df["marks"].min())
print("average marks:",df["marks"].mean())
print("total student:",df["marks"].count())
