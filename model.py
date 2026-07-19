# import pandas as pd
# from sklearn.linear_model import LinearRegression

# class MLModel:

#     def __init__(self, target_column):
#         self.target_column = target_column
#         self.model = LinearRegression()

#     def train(self):
#         train = pd.read_json("output/cleaned_train.json")
#         # Convert text columns to numbers
#         train = pd.get_dummies(train)
#         # Target
#         y_train = train[self.target_column]
#         # Features
#         X_train = train.drop(self.target_column, axis=1)
#         self.model.fit(X_train, y_train)
#         self.columns = X_train.columns
#         print("Model Trained Successfully!")

#     def predict(self):
#         test = pd.read_json("output/cleaned_test.json")
#     # Convert text columns to numbers
#         test = pd.get_dummies(test)
#     # Make test columns match train columns
#         test = test.reindex(columns=self.columns, fill_value=0)
#         predictions = self.model.predict(test)
#         print("\nPredicted Prices:")
#         print(predictions)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from exporter import ExportData


class MachineLearningModel:

    def __init__(self, data, target_column):

        self.data = data
        self.target_column = target_column
        self.model = None

    def encode_data(self):

        categorical_columns = self.data.select_dtypes(
            include=["object", "category", "string"]
        ).columns

        for column in categorical_columns:
            self.data[column] = LabelEncoder().fit_transform(
                self.data[column].astype(str)
            )

        print("Data Encoded Successfully!")

    def split_data(self):

        X = self.data.drop(self.target_column, axis=1)
        y = self.data[self.target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42
        )

        return X_train, X_test, y_train, y_test

    def train_model(self):

        self.encode_data()

        X_train, X_test, y_train, y_test = self.split_data()

        self.model = RandomForestClassifier()

        self.model.fit(X_train, y_train)

        prediction = self.model.predict(X_test)

        accuracy = accuracy_score(y_test, prediction)

        print("Model Trained Successfully!")
        print("Accuracy:", accuracy)

        exporter = ExportData()
        exporter.save_predictions(prediction)
        exporter.save_predictions_json(prediction)