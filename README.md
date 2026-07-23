# Bank Marketing Prediction

## Project

This project is a Machine Learning classification project. It predicts whether a customer will subscribe to a bank term deposit using the Bank Marketing dataset.

The project is developed using Python and the CatBoost Classifier.

---

## Files

- **main.py** – Runs the project.
- **cleaner.py** – Cleans and prepares the dataset.
- **model.py** – Trains the machine learning model and makes predictions.
- **exporter.py** – Saves the predictions and confusion matrix.

---

## Libraries Used

- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- CatBoost

---

## Project Steps

1. Load the dataset.
2. Clean the data.
3. Handle missing values and duplicates.
4. Split the dataset into training and testing data.
5. Train the CatBoost model.
6. Make predictions.
7. Evaluate the model.
8. Save the results.

---

## Output Files

After running the project, these files will be created:

- `train.json`
- `test.json`
- `predictions.csv`
- `predictions.json`
- `confusion_matrix.png`
- `model.cbm`

---

## Evaluation

The model performance is measured using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

---

## How to Run

Install the required libraries:

```bash
pip install pandas matplotlib seaborn scikit-learn catboost
```

Run the project:

```bash
python main.py
```

---

## Author

**Safoora Chaudhry**
