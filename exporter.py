# import pandas as pd

# class Exporter:

#     def __init__(self, df):
#         self.df = df

#     # Save data as JSON
#     def save_json(self, filename):
#         self.df.to_json(filename, orient="records", indent=4)
#         print(f"{filename} saved successfully.")
import pandas as pd


class ExportData:

    def __init__(self):
        pass

    # Save Predictions
    def save_predictions(self, predictions):

        prediction_data = pd.DataFrame(predictions, columns=["Prediction"])

        prediction_data.to_csv(
            "output/predictions.csv",
            index=False
        )

        print("Predictions saved successfully!")

    # Save as JSON
    def save_predictions_json(self, predictions):

        prediction_data = pd.DataFrame(predictions, columns=["Prediction"])

        prediction_data.to_json(
            "output/predictions.json",
            orient="records",
            indent=4
        )

        print("Predictions JSON saved successfully!")