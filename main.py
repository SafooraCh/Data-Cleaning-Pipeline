import pandas as pd

# Load the dataset
df = pd.read_csv("input/dirty_cafe_sales1.csv", encoding="latin1")

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display shape
print("\nDataset Shape:")
print(df.shape)

# Display columns
print("\nColumns:")
print(df.columns.tolist())

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())