
import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

from catboost import CatBoostClassifier

from exporter import ExportData


class MachineLearningModel:

    def __init__(
        self,
        data,
        target_column
    ):

        self.data = data.copy()

        self.target_column = target_column

        self.model = None

        self.X_train = None
        self.X_test = None

        self.y_train = None
        self.y_test = None

        self.predictions = None

    # ==========================================
    # Split Dataset ONCE
    # ==========================================
    def split_data(self):

        if self.target_column not in self.data.columns:

            raise ValueError(
                f"Target column '{self.target_column}' not found."
            )

        X = self.data.drop(
            columns=[self.target_column]
        )

        y = self.data[
            self.target_column
        ]

        # Make sure target is binary
        if y.nunique() != 2:

            raise ValueError(
                "This project expects a binary classification target."
            )

        # Identify categorical columns
        categorical_columns = X.select_dtypes(
            include=["object", "category", "string"]
        ).columns.tolist()

        # Convert categorical values to string
        for col in categorical_columns:

            X[col] = X[col].astype(str)

        # Split ONCE
        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test
        ) = train_test_split(

            X,
            y,

            test_size=0.20,

            random_state=42,

            stratify=y
        )

        print("\nDataset Split Successfully!")

        print(
            f"Training Samples: {len(self.X_train)}"
        )

        print(
            f"Testing Samples: {len(self.X_test)}"
        )

        return categorical_columns

    # ==========================================
    # Export Same Train/Test Split
    # ==========================================
    def export_train_test_data(self):

        os.makedirs(
            "data",
            exist_ok=True
        )

        train_data = self.X_train.copy()

        train_data[
            self.target_column
        ] = self.y_train.values

        test_data = self.X_test.copy()

        test_data[
            self.target_column
        ] = self.y_test.values

        train_data.to_json(
            "data/train.json",
            orient="records",
            indent=4
        )

        test_data.to_json(
            "data/test.json",
            orient="records",
            indent=4
        )

        print(
            "Train and test datasets exported successfully!"
        )

    # ==========================================
    # Train CatBoost Model
    # ==========================================
    def train_model(self):

        # Split only once
        categorical_columns = self.split_data()

        # Save exact same split
        self.export_train_test_data()

        # Get categorical column indices
        categorical_indices = [
            self.X_train.columns.get_loc(col)
            for col in categorical_columns
        ]

        # Create model
        self.model = CatBoostClassifier( iterations=500,learning_rate=0.05,depth=8,loss_function="Logloss",eval_metric="Accuracy",random_seed=42,verbose=0)

        # Train model
        self.model.fit(

            self.X_train,

            self.y_train,

            cat_features=categorical_indices
        )

        print(
            "\n===================================="
        )

        print(
            "CATBOOST MODEL TRAINED SUCCESSFULLY"
        )

        print(
            "===================================="
        )

        # Predictions
        self.predictions = (
            self.model.predict(
                self.X_test
            ).flatten()
        )

        # ======================================
        # Evaluation
        # ======================================

        accuracy = accuracy_score(
            self.y_test,
            self.predictions
        )

        precision = precision_score(
            self.y_test,
            self.predictions,
            pos_label="yes",
            zero_division=0
        )

        recall = recall_score(
            self.y_test,
            self.predictions,
            pos_label="yes",
            zero_division=0
        )

        f1 = f1_score(
            self.y_test,
            self.predictions,
            pos_label="yes",
            zero_division=0
        )

        confusion = confusion_matrix(
            self.y_test,
            self.predictions,
            labels=["no", "yes"]
        )

        report = classification_report(
            self.y_test,
            self.predictions,
            zero_division=0
        )

        # ======================================
        # Print Results
        # ======================================

        print(
            f"\nAccuracy: {accuracy:.4f}"
        )

        print(
            f"Precision: {precision:.4f}"
        )

        print(
            f"Recall: {recall:.4f}"
        )

        print(
            f"F1-Score: {f1:.4f}"
        )

        print(
            "\nConfusion Matrix:"
        )

        print(
            confusion
        )

        print(
            "\nClassification Report:"
        )

        print(
            report
        )

        # ======================================
        # Save Model
        # ======================================

        os.makedirs(
            "output",
            exist_ok=True
        )

        self.model.save_model(
            "output/model.cbm"
        )

        print(
            "\nModel saved successfully!"
        )

        # ======================================
        # Export Predictions
        # ======================================

        exporter = ExportData()

        exporter.save_predictions(

            test_data=self.X_test,

            actual_values=self.y_test,

            predictions=self.predictions
        )

        # ======================================
        # Save Confusion Matrix
        # ======================================

        exporter.save_confusion_matrix(
            confusion
        )

        print(
            "\nPredictions saved successfully!"
        )