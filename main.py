# 
from cleaner import DataCleaner
from model import MachineLearningModel


# ==========================================
# Configuration
# ==========================================

file_path = "input/bank.csv"

target_column = "deposit"


# ==========================================
# Data Cleaning Pipeline
# ==========================================

cleaner = DataCleaner(
    file_path
)


# Load Dataset
cleaner.load_data()


# Validate Dataset
cleaner.validate_dataset()


# Display First 5 Rows
cleaner.display_data()


# Dataset Information
cleaner.dataset_info()


# Check Missing Values
cleaner.check_missing_values()


# Check Duplicate Rows
cleaner.check_duplicates()


# Remove Duplicate Rows
cleaner.remove_duplicates()


# Handle Missing Values
cleaner.handle_missing_values()


# Fix Data Types
cleaner.fix_data_types()


# Handle Outliers
# Uses IQR Capping Instead of Deleting Rows
cleaner.handle_outliers()


# Statistical Summary
cleaner.statistical_summary()


# Unique Values
cleaner.unique_values()


# Visualize Data
cleaner.visualize_data()


# Save Clean Dataset
cleaner.save_clean_dataset()


# ==========================================
# Machine Learning Pipeline
# ==========================================

model = MachineLearningModel(

    cleaner.data,

    target_column
)


# Train and Evaluate Model
model.train_model()


print(
    "\n===================================="
)

print(
    "COMPLETE PIPELINE EXECUTED SUCCESSFULLY"
)

print(
    "===================================="
)