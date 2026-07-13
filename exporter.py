import pandas as pd

class Exporter:

    def __init__(self, df):
        self.df = df

    # Save data as CSV
    def save_csv(self):
        self.df.to_csv("cleaned_data.csv", index=False)
        print("CSV file saved successfully.")

    # Save data as JSON
    def save_json(self):
        self.df.to_json("cleaned_data.json", orient="records", indent=4)
        print("JSON file saved successfully.")