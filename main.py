from cleaner import DataCleaner
from exporter import Exporter
cleaner = DataCleaner("input/hotel_bookings.csv")
cleaner.load_data()
cleaner.dataset_info()
cleaner.check_missing_values()
cleaner.check_duplicates()
cleaner.remove_duplicates()
cleaner.handle_missing_values()
cleaner.fix_data_types()
cleaner.statistical_summary()
cleaner.save_data()
 # Export File
export = Exporter(cleaner.df)
export.save_csv()
export.save_json()
# cleaner.clean_installs()
# cleaner.clean_price()
# cleaner.clean_size()
# cleaner.clean_reviews()


# print("\nAfter Cleaning:")
# cleaner.check_missing_values()

