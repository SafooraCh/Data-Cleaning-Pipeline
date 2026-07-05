class Exporter:

    def __init__(self, df):
        self.df = df

    def export_csv(self):
        self.df.to_csv("output/cleaned_googleplaystore.csv", index=False)
        print("CSV File Exported Successfully!")

    def export_json(self):
        self.df.to_json(
            "output/cleaned_googleplaystore.json",
            orient="records",
            indent=4
        )
        print("JSON File Exported Successfully!")