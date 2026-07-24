import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataCleaner:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

        self.required_columns = [
            "age",
            "job",
            "marital",
            "education",
            "default",
            "balance",
            "housing",
            "loan",
            "contact",
            "day",
            "month",
            "duration",
            "campaign",
            "pdays",
            "previous",
            "poutcome",
            "deposit"
        ]

        self.numerical_columns = [
            "age",
            "balance",
            "day",
            "duration",
            "campaign",
            "pdays",
            "previous"
        ]

    # ==========================================
    # Load Dataset
    # ==========================================
    def load_data(self):

        if not os.path.exists(self.file_path):
            raise FileNotFoundError(
                f"Dataset not found: {self.file_path}"
            )

        if self.file_path.lower().endswith(".csv"):
            self.data = pd.read_csv(self.file_path)

        elif self.file_path.lower().endswith(".json"):
            self.data = pd.read_json(self.file_path)

        else:
            raise ValueError(
                "Only CSV and JSON files are supported."
            )

        print("Dataset Loaded Successfully!")

        return self.data

    # ==========================================
    # Validate Dataset Structure
    # ==========================================
    def validate_dataset(self):

        if self.data is None:
            raise ValueError(
                "Dataset is not loaded."
            )

        missing_columns = [
            col for col in self.required_columns
            if col not in self.data.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        print("Dataset structure validated successfully!")

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
    # Check Missing Values
    # ==========================================
    def check_missing_values(self):

        print("\nMissing Values")
        print(self.data.isnull().sum())

    # ==========================================
    # Handle Missing Values
    # ==========================================
    def handle_missing_values(self):

        numerical_columns = self.data.select_dtypes(
            include=["number"]
        ).columns

        categorical_columns = self.data.select_dtypes(
            exclude=["number"]
        ).columns

        # Numerical → Median
        for col in numerical_columns:

            if self.data[col].isnull().any():

                self.data[col] = self.data[col].fillna(
                    self.data[col].median()
                )

        # Categorical → Mode
        for col in categorical_columns:

            if self.data[col].isnull().any():

                mode_value = self.data[col].mode()

                if not mode_value.empty:

                    self.data[col] = self.data[col].fillna(
                        mode_value[0]
                    )

        print("Missing values handled successfully!")

    # ==========================================
    # Check Duplicate Rows
    # ==========================================
    def check_duplicates(self):

        duplicate_count = self.data.duplicated().sum()

        print(
            f"\nDuplicate Rows: {duplicate_count}"
        )

    # ==========================================
    # Remove Duplicate Rows
    # ==========================================
    def remove_duplicates(self):

        before = len(self.data)

        self.data = self.data.drop_duplicates().reset_index(
            drop=True
        )

        after = len(self.data)

        print(
            f"Removed {before - after} duplicate rows."
        )
        def visualize_data(self):
                 # ==========================================
                # Boxplots of Numerical Features
                # ==========================================
        
                numerical_columns = [
                    "age",
                    "balance",
                    "day",
                    "duration",
                    "campaign",
                    "pdays",
                    "previous"
                ]
        
                plt.figure(figsize=(15, 10))
        
                for i, column in enumerate(numerical_columns, 1):
        
                    plt.subplot(3, 3, i)
        
                    sns.boxplot(
                        x=self.data[column]
                    )
        
                    plt.title(column)
        
                plt.tight_layout()
        
                plt.savefig("output/boxplots.png")
        
                plt.close()
        
                print("Boxplots Saved Successfully!")

    # ==========================================
    # Handle Outliers Using IQR Capping
    # ==========================================
    def handle_outliers(self):

        for column in self.numerical_columns:

            if column not in self.data.columns:
                continue

            q1 = self.data[column].quantile(0.25)
            q3 = self.data[column].quantile(0.75)

            iqr = q3 - q1

            lower_bound = q1 - (1.5 * iqr)
            upper_bound = q3 + (1.5 * iqr)

            # Cap instead of removing rows
            self.data[column] = self.data[column].clip(
                lower=lower_bound,
                upper=upper_bound
            )

        print(
            "Outliers handled successfully using IQR capping!"
        )

    # ==========================================
    # Check Data Types
    # ==========================================
    def fix_data_types(self):

        integer_columns = [
            "age",
            "balance",
            "day",
            "duration",
            "campaign",
            "pdays",
            "previous"
        ]

        for col in integer_columns:

            if col in self.data.columns:

                self.data[col] = pd.to_numeric(
                    self.data[col],
                    errors="coerce"
                )

        # Target as string
        if "deposit" in self.data.columns:

            self.data["deposit"] = (
                self.data["deposit"]
                .astype(str)
                .str.lower()
                .str.strip()
            )

        print(
            "Data types checked successfully!"
        )

    # ==========================================
    # Unique Values
    # ==========================================
    def unique_values(self):

        print("\nUnique Values")

        for col in self.data.columns:

            print(
                f"{col}: {self.data[col].nunique()}"
            )

    # ==========================================
    # Statistical Summary
    # ==========================================
    def statistical_summary(self):

        print("\nStatistical Summary")

        print(
            self.data.describe(
                include="all"
            )
        )

    # ==========================================
    # Visualize Data
    # ==========================================
    def visualize_data(self):

        os.makedirs(
            "output",
            exist_ok=True
        )

        # --------------------------------------
        # Histograms
        # --------------------------------------
        self.data.hist(
            figsize=(12, 8)
        )

        plt.suptitle(
            "Histogram of Numerical Features"
        )

        plt.tight_layout()

        plt.savefig(
            "output/histograms.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        # --------------------------------------
        # Correlation Heatmap
        # --------------------------------------
        numerical_data = self.data.select_dtypes(
            include=["number"]
        )

        plt.figure(
            figsize=(10, 8)
        )

        correlation = numerical_data.corr()

        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )

        plt.title(
            "Correlation Heatmap"
        )

        plt.tight_layout()

        plt.savefig(
            "output/correlation_heatmap.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        # --------------------------------------
        # Deposit Distribution
        # --------------------------------------
        plt.figure(
            figsize=(6, 4)
        )

        sns.countplot(
            data=self.data,
            x="deposit"
        )

        plt.title(
            "Deposit Distribution"
        )

        plt.tight_layout()

        plt.savefig(
            "output/deposit_distribution.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        # --------------------------------------
        # Age vs Balance
        # --------------------------------------
        plt.figure(
            figsize=(7, 5)
        )

        sns.scatterplot(
            data=self.data,
            x="age",
            y="balance",
            hue="deposit"
        )

        plt.title(
            "Age vs Balance"
        )

        plt.tight_layout()

        plt.savefig(
            "output/age_vs_balance.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(
            "Visualizations saved successfully!"
        )
       

    # ==========================================
    # Save Clean Dataset
    # ==========================================
    def save_clean_dataset(self):

        os.makedirs(
            "output",
            exist_ok=True
        )

        self.data.to_csv(
            "output/cleaned_dataset.csv",
            index=False
        )

        self.data.to_json(
            "output/cleaned_dataset.json",
            orient="records",
            indent=4
        )

        print(
            "Clean dataset saved successfully!"
        )