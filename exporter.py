import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ExportData:

    def __init__(self):
        os.makedirs("output", exist_ok=True)

    # Save Predictions
    def save_predictions(self, test_data, actual_values, predictions):

        # Copy test data
        prediction_data = test_data.copy()

        # Add new columns
        prediction_data["Actual"] = actual_values
        prediction_data["Prediction"] = predictions

        # Save files
        prediction_data.to_csv("output/predictions.csv", index=False)
        prediction_data.to_json("output/predictions.json", orient="records", indent=4)

        print("Predictions Saved Successfully!")

    # Save Confusion Matrix
    def save_confusion_matrix(self, confusion):

        plt.figure(figsize=(6,5))

        sns.heatmap(
            confusion,
            annot=True,
            cmap="Blues",
            fmt="d"
        )

        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix")

        plt.savefig("output/confusion_matrix.png")
        plt.close()

        print("Confusion Matrix Saved Successfully!")
        