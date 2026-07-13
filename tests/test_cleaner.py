import sys
import os

# Add project folder to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from cleaner import DataCleaner


def test_load_data():
    cleaner = DataCleaner("input/hotel_bookings.csv")
    cleaner.load_data()

    assert cleaner.df is not None
    print("✅ Test Passed: Dataset Loaded Successfully!")


def test_remove_duplicates():
    cleaner = DataCleaner("input/hotel_bookings.csv")
    cleaner.load_data()

    before = len(cleaner.df)

    cleaner.remove_duplicates()

    after = len(cleaner.df)

    assert after <= before
    print("✅ Test Passed: Duplicates Removed Successfully!")


test_load_data()
test_remove_duplicates()