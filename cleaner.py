# import pandas as pd

# class DataCleaner:

#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.df = None

#     # Load Dataset
#     def load_data(self):
#         self.df = pd.read_json(self.file_path)
#         print("Dataset Loaded Successfully!")

#     # Dataset Information
#     def dataset_info(self):
#         print("\nShape:", self.df.shape)
#         print("\nColumns:")
#         print(self.df.columns)
#         print("\nFirst 10 Rows:")
#         print(self.df.head(10))

#     # Check Missing Values
#     def check_missing_values(self):
#         print("\nMissing Values:")
#         print(self.df.isnull().sum())

#     # Handle Missing Values
#     def handle_missing_values(self):
#         for column in self.df.columns:
#             if self.df[column].dtype == "object":
#                 self.df[column] = self.df[column].fillna(self.df[column].mode()[0])
#             else:
#                 self.df[column] = self.df[column].fillna(0)

#         print("\nMissing Values After Handling:")
#         print(self.df.isnull().sum())

#     # Check Duplicate Rows
#     def check_duplicates(self):
#         print("\nDuplicate Rows:", self.df.duplicated().sum())

#     # Remove Duplicate Rows
#     def remove_duplicates(self):
#         self.df.drop_duplicates(inplace=True)
#         print("\nDuplicates Removed!")

#     # Fix Data Types
#     def fix_data_types(self):
#         for column in self.df.columns:

#             # Convert object columns to numeric
#             if self.df[column].dtype == "object":
#                 try:
#                     self.df[column] = pd.to_numeric(self.df[column])
#                 except:
#                     pass

#             # Convert object columns to datetime
#             if self.df[column].dtype == "object":
#                 try:
#                     self.df[column] = pd.to_datetime(self.df[column])
#                 except:
#                     pass

#             # Convert Yes/No or True/False to Boolean
#             if self.df[column].dtype == "object":
#                 unique_values = self.df[column].dropna().astype(str).str.lower().unique()

#                 if set(unique_values).issubset({"yes", "no"}):
#                     self.df[column] = self.df[column].map({"yes": True, "no": False})

#                 elif set(unique_values).issubset({"true", "false"}):
#                     self.df[column] = self.df[column].map({"true": True, "false": False})

#         print("\nData Types Fixed Successfully!")
#         print(self.df.dtypes)

#     # Statistical Summary
#     def statistical_summary(self):
#         print("\nStatistical Summary:")
#         print(self.df.describe())

#     # Save Dataset
#     def save_data(self):
#         self.df.to_json("output/cleaned_data.json", orient="records", indent=4)
#         print("\nCleaned Dataset Saved Successfully!")

        
    # # Clean Installs Column
    # def clean_installs(self):
    #     self.df["Installs"] = self.df["Installs"].str.replace(",", "", regex=False)
    #     self.df["Installs"] = self.df["Installs"].str.replace("+", "", regex=False)
    #     self.df["Installs"] = pd.to_numeric(self.df["Installs"], errors="coerce")
    #     print("\nInstalls Cleaned!")

    # # Clean Price Column
    # def clean_price(self):
    #     self.df["Price"] = self.df["Price"].str.replace("$", "", regex=False)
    #     self.df["Price"] = pd.to_numeric(self.df["Price"], errors="coerce")
    #     print("\nPrice Cleaned!")

    # # Clean Size Column
    # def clean_size(self):
    #     self.df["Size"] = self.df["Size"].replace("Varies with device", pd.NA)
    #     self.df["Size"] = self.df["Size"].str.replace("M", "", regex=False)
    #     self.df["Size"] = self.df["Size"].str.replace("k", "", regex=False)
    #     self.df["Size"] = pd.to_numeric(self.df["Size"], errors="coerce")
    #     print("\nSize Cleaned!")

    # # Clean Reviews Column
    # def clean_reviews(self):
    #     self.df["Reviews"] = pd.to_numeric(self.df["Reviews"], errors="coerce")
    #     print("\nReviews Cleaned!")

    # # Handle Missing Values
    # def handle_missing_values(self):
    #     self.df["Rating"] = self.df["Rating"].fillna(self.df["Rating"].mean())
    #     self.df["Type"] = self.df["Type"].fillna("Unknown")
    #     self.df["Content Rating"] = self.df["Content Rating"].fillna("Unknown")
    #     self.df["Current Ver"] = self.df["Current Ver"].fillna("Unknown")
    #     self.df["Android Ver"] = self.df["Android Ver"].fillna("Unknown")
    #     print("\nMissing Values Handled!")

    # # Dataset Summary
    # def summary(self):
    #     print("\n===== DATASET SUMMARY =====")
    #     print("Rows:", self.df.shape[0])
    #     print("Columns:", self.df.shape[1])

    #     print("\nData Types:")
    #     print(self.df.dtypes)

    # # Save Dataset
    # def save_data(self):
    #     self.df.to_csv("output/cleaned_googleplaystore.csv", index=False)
    #     print("\nCleaned Dataset Saved Successfully!")
import os
import pandas as pd
from sklearn.model_selection import train_test_split


class DataCleaner:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    # ==========================================
    # Load Dataset
    # ==========================================
    def load_data(self):

        if self.file_path.endswith(".csv"):
            self.data = pd.read_csv(self.file_path)

        elif self.file_path.endswith(".json"):
            self.data = pd.read_json(self.file_path)

        else:
            print("Only CSV and JSON files are supported.")
            return

        print("Dataset Loaded Successfully!")
        return self.data

    # ==========================================
    # Convert CSV to JSON
    # ==========================================
    def convert_csv_to_json(self):

        if self.data is None:
            print("Please load the dataset first.")
            return

        train_data, test_data = train_test_split(
            self.data,
            test_size=0.20,
            random_state=42
        )

        os.makedirs("data", exist_ok=True)

        train_data.to_json(
            "data/train.json",
            orient="records",
            indent=4
        )

        test_data.to_json(
            "data/test.json",
            orient="records",
            indent=4
        )

        print("CSV converted to train.json and test.json successfully!")

    # ==========================================
    # Display First 5 Rows
    # ==========================================
    def display_data(self):

        print("\nFirst 5 Rows")
        print(self.data.head())
    
    # ==========================================
    # Dataset Information
    # ==========================================
    def dataset_info(self):

        print("\nDataset Information")
        self.data.info()

        print("\nShape:")
        print(self.data.shape)

        print("\nColumn Names:")
        print(self.data.columns.tolist())

     # ==========================================
    # Handle Outliers (IQR Method)
    # ==========================================
    def handle_outliers(self):

        columns = ["age", "balance", "day", "duration", "campaign", "previous"]

        for column in columns:

            Q1 = self.data[column].quantile(0.25)
            Q3 = self.data[column].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - (1.5 * IQR)
            upper = Q3 + (1.5 * IQR)

            self.data = self.data[
                (self.data[column] >= lower) &
                (self.data[column] <= upper)
            ]

        print("Outliers handled successfully!")

    # ==========================================
    # Data Types
    # ==========================================
    def data_types(self):

        print("\nData Types")
        print(self.data.dtypes)

    # ==========================================
    # Check Missing Values
    # ==========================================
    def check_missing_values(self):

        print("\nMissing Values")
        print(self.data.isnull().sum())

    # ==========================================
    # Check Duplicate Rows
    # ==========================================
    def check_duplicates(self):

        duplicates = self.data.duplicated().sum()

        print("\nDuplicate Rows:", duplicates)

    # ==========================================
    # Remove Duplicate Rows
    # ==========================================
    def remove_duplicates(self):

        before = len(self.data)

        self.data.drop_duplicates(inplace=True)

        after = len(self.data)

        print("Removed", before - after, "duplicate rows.")

    # ==========================================
    # Handle Missing Values
    # ==========================================
    def handle_missing_values(self):

        # Numerical Columns
        numerical_columns = self.data.select_dtypes(include="number").columns

        for column in numerical_columns:
            self.data[column] = self.data[column].fillna(
                self.data[column].median()
            )

        # Categorical Columns
        categorical_columns = self.data.select_dtypes(exclude="number").columns

        for column in categorical_columns:
            self.data[column] = self.data[column].fillna(
                self.data[column].mode()[0]
            )

        print("Missing values handled successfully!")

    # ==========================================
    # Fix Data Types
    # ==========================================
    def fix_data_types(self):

        for column in self.data.columns:

            try:
                self.data[column] = pd.to_numeric(self.data[column])

            except:
                pass

        print("Data types checked successfully!")

    # ==========================================
    # Unique Values
    # ==========================================
    def unique_values(self):

        print("\nUnique Values")

        for column in self.data.columns:
            print(column, ":", self.data[column].nunique())

    # ==========================================
    # Statistical Summary
    # ==========================================
    def statistical_summary(self):

        print("\nStatistical Summary")
        print(self.data.describe(include="all"))

    # ==========================================
    # Save Clean Dataset
    # ==========================================
    def save_clean_dataset(self):

        os.makedirs("output", exist_ok=True)

        self.data.to_csv(
            "output/cleaned_dataset.csv",
            index=False
        )

        self.data.to_json(
            "output/cleaned_dataset.json",
            orient="records",
            indent=4
        )

        print("Clean dataset saved successfully!")