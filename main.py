from cleaner import DataCleaner
# from exporter import Exporter
cleaner = DataCleaner("input/googleplaystore.csv")
cleaner.load_data()
cleaner.dataset_info()
cleaner.check_missing_values()
cleaner.check_duplicates()
cleaner.remove_duplicates()
cleaner.handle_missing_values()
cleaner.fix_data_types()
cleaner.statistical_summary()
# cleaner.clean_installs()
# cleaner.clean_price()
# cleaner.clean_size()
# cleaner.clean_reviews()


# print("\nAfter Cleaning:")
# cleaner.check_missing_values()

# cleaner.save_data()
# cleaner.summary()
# # Export Files
# exporter = Exporter(cleaner.df)
# exporter.export_csv()
# exporter.export_json()