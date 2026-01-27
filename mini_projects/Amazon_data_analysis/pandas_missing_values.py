import pandas as pd
df = pd.read_csv("amazon.csv")
print("total number of null values:")
print(df.isnull().sum())
