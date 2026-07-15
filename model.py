import pandas as pd
from sklearn.linear_model import LinearRegression

class MLModel:

    def __init__(self, target_column):
        self.target_column = target_column
        self.model = LinearRegression()

    def train(self):

        train = pd.read_json("output/cleaned_train.json")

        # Convert text columns to numbers
        train = pd.get_dummies(train)

        # Target
        y_train = train[self.target_column]

        # Features
        X_train = train.drop(self.target_column, axis=1)

        self.model.fit(X_train, y_train)

        self.columns = X_train.columns

        print("Model Trained Successfully!")
    def predict(self):

        test = pd.read_json("output/cleaned_test.json")

    # Convert text columns to numbers
        test = pd.get_dummies(test)

    # Make test columns match train columns
        test = test.reindex(columns=self.columns, fill_value=0)

        predictions = self.model.predict(test)

        print("\nPredicted Prices:")
        print(predictions)