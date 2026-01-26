import pandas as pd
df=pd.read_csv("students.txt",header=None,names=["roll","name","marks"])
topper=df[df["marks"]==df["marks"].max()]
print("topper:",topper)
