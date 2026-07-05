# Data Cleaning Pipeline

## Project Overview

This project is a simple Data Cleaning Pipeline developed using **Python**, **Pandas**, and **Object-Oriented Programming (OOP)**. It cleans the Google Play Store dataset by handling missing values, removing duplicate records, cleaning columns, and exporting the cleaned data.

---

## Features

- Load dataset
- Display dataset information
- Check missing values
- Check duplicate records
- Remove duplicates
- Clean Installs column
- Clean Price column
- Clean Size column
- Clean Reviews column
- Handle missing values
- Display dataset summary
- Export cleaned dataset to CSV
- Export cleaned dataset to JSON

---

## Technologies Used

- Python
- Pandas
- Object-Oriented Programming (OOP)

---

## Project Structure

```
Data-Cleaning-Pipeline/
│
├── input/
│   └── googleplaystore.csv
│
├── output/
│   ├── cleaned_googleplaystore.csv
│   └── cleaned_googleplaystore.json
│
├── tests/
│   └── test_cleaner.py
│
├── cleaner.py
├── exporter.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Dataset

**Dataset Name:** Google Play Store Apps

Source: Kaggle

The dataset contains information about Android applications available on the Google Play Store.

---

## Data Cleaning Steps

1. Load the dataset
2. Display dataset information
3. Check missing values
4. Check duplicate records
5. Remove duplicate records
6. Clean the Installs column
7. Clean the Price column
8. Clean the Size column
9. Clean the Reviews column
10. Handle missing values
11. Display dataset summary
12. Save cleaned dataset

---

## How to Run

### Clone the repository

```bash
git clone <repository-url>
```

### Move to project folder

```bash
cd Data-Cleaning-Pipeline
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python main.py
```

---

## Output

The cleaned files are saved in the **output** folder.

```
cleaned_googleplaystore.csv
cleaned_googleplaystore.json
```

---

## OOP Classes

### DataCleaner

Responsible for:

- Loading data
- Cleaning data
- Handling missing values
- Removing duplicates
- Saving cleaned dataset

### Exporter

Responsible for:

- Exporting CSV file
- Exporting JSON file

---

## Sample Output

```
Dataset Loaded Successfully!

Duplicates Removed!

Installs Cleaned!

Price Cleaned!

Size Cleaned!

Reviews Cleaned!

Missing Values Handled!

Cleaned Dataset Saved Successfully!

CSV File Exported Successfully!

JSON File Exported Successfully!
```

---

## Author

**Safoora**

BS Artificial Intelligence Student

---

## License

This project is created for learning and educational purposes.