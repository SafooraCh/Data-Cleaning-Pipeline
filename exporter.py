import pandas as pd

class Exporter:

    def __init__(self, df):
        self.df = df

    # Save data as JSON
    def save_json(self, filename):
        self.df.to_json(filename, orient="records", indent=4)
        print(f"{filename} saved successfully.")