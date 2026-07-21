# from cleaner import DataCleaner
# from exporter import Exporter
# from model import MLModel
# # -------------------- Train Dataset --------------------

# train_cleaner = DataCleaner("input/train.json")
# train_cleaner.load_data()
# train_cleaner.dataset_info()
# train_cleaner.check_missing_values()
# train_cleaner.check_duplicates()
# train_cleaner.remove_duplicates()
# train_cleaner.handle_missing_values()
# train_cleaner.fix_data_types()
# train_cleaner.statistical_summary()

# train_export = Exporter(train_cleaner.df)
# train_export.save_json("output/cleaned_train.json")


# -------------------- Test Dataset --------------------

# test_cleaner = DataCleaner("input/test.json")

# test_cleaner.load_data()
# test_cleaner.dataset_info()
# test_cleaner.check_missing_values()
# test_cleaner.check_duplicates()
# test_cleaner.remove_duplicates()
# test_cleaner.handle_missing_values()
# test_cleaner.fix_data_types()
# test_cleaner.statistical_summary()

# test_export = Exporter(test_cleaner.df)
# test_export.save_json("output/cleaned_test.json")

# model = MLModel("SalePrice")

# model.train()
# model.predict()
from cleaner import DataCleaner
from model import MachineLearningModel
from exporter import ExportData

# Dataset Path
file_path = "input/bank.csv"

# Target Column
target_column = "deposit"


# Create Object
cleaner = DataCleaner(file_path)

# Load Dataset
cleaner.load_data()

# Convert CSV to JSON
cleaner.convert_csv_to_json()

# Display Dataset
cleaner.display_data()

# Dataset Information
cleaner.dataset_info()

# Missing Values
cleaner.check_missing_values()

# Duplicate Rows
cleaner.check_duplicates()

# Remove Duplicates
cleaner.remove_duplicates()
# Handle Outliers
cleaner.handle_outliers() 

# Handle Missing Values
cleaner.handle_missing_values()

# Fix Data Types
cleaner.fix_data_types()

# Summary
cleaner.statistical_summary()

# Save Clean Dataset
cleaner.save_clean_dataset()


# Machine Learning
model = MachineLearningModel(cleaner.data, target_column)

model.train_model()