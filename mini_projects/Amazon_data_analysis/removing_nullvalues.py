import pandas as pd
df = pd.read_csv("amazon.csv")
df =  df.dropna(subset=["rating_count"])
print(df.isnull().sum())
