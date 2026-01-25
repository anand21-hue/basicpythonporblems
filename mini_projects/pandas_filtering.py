import pandas as pd

df = pd.read_csv("students.txt", header=None, names=["roll", "name", "marks"])

print("Students scoring above 80:")
print(df[df["marks"] > 80])
