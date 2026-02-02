import pandas as pd

# For a CSV file
df = pd.read_csv('amazon.csv')
# For an Excel file
# df = pd.read_excel('your_dataset.xlsx')

# Get column names
column_names = list(df.columns)

# Print the column names
print("Column names:", column_names)
