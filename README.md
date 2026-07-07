# Duplicate Rows Detection & Removal

## Overview

Duplicate records are repeated rows that contain the same information. These duplicates can negatively impact data analysis, visualization, and machine learning models by introducing redundancy and bias.

This module identifies duplicate rows in a dataset and removes them while keeping the first occurrence, resulting in a cleaner and more reliable dataset.

---

## Objective

- Detect duplicate rows in the dataset.
- Display the total number of duplicate records.
- Remove duplicate rows.
- Improve overall data quality.
- Prepare the dataset for further preprocessing and analysis.

---

## Implementation

The duplicate handling process is implemented using the Pandas library.

### Methods Used

- `duplicated()` – Identifies duplicate rows.
- `drop_duplicates()` – Removes duplicate rows while retaining the first occurrence.

---

## Functions

### `check_duplicates()`

This function:

- Counts duplicate rows.
- Displays the total number of duplicates found.
- Helps identify redundant records before cleaning.

### `remove_duplicates()`

This function:

- Removes duplicate rows from the dataset.
- Displays the dataset size before cleaning.
- Displays the dataset size after cleaning.
- Reports the number of duplicate rows removed.

---

## Example

```python
cleaner.load_data()

cleaner.check_duplicates()

cleaner.remove_duplicates()
```

---

## Sample Output

```text
========== DUPLICATE ROWS ==========
Duplicate Rows Found : 483

========== REMOVING DUPLICATES ==========
Rows Before Cleaning : 10841
Rows After Cleaning  : 10358
Duplicate Rows Removed : 483

Duplicate removal completed successfully!
```

---

## Benefits

- Eliminates redundant records.
- Improves data consistency.
- Prevents duplicate data from affecting analysis.
- Enhances machine learning model performance.
- Reduces unnecessary storage usage.
- Produces a cleaner and more reliable dataset.

---

## Technologies Used

- Python 3
- Pandas

---

## Files

```
Data-Cleaning-Pipeline/
│
├── data/
│   └── dataset.csv
│
├── main.py
├── data_cleaner.py
├── README.md
└── requirements.txt
```

---

## Conclusion

Duplicate row detection and removal is an essential step in any data cleaning pipeline. By eliminating redundant records, the dataset becomes more accurate, consistent, and ready for data analysis, visualization, and machine learning applications.