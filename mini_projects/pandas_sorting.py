import pandas as pd
df=pd.read_csv("students.txt",header=None,names=["roll","name","marks"])
print("sorting grouping(highest first)")
print(df.sort_values(by="marks",ascending=False))
