# data_cleaning_task1
Internship Task 1 — Data Cleaning and Preprocessing using Pandas

# 🧹 Data Cleaning and Preprocessing — Internship Task 1

This project is part of my **Data Analyst Internship Task 1**, where I performed data cleaning and preprocessing using **Python (Pandas)**.  
The goal was to clean a raw dataset containing missing values, duplicates, inconsistent formats, and mixed data types.

---

## 📂 Files Included
| File Name | Description |
|------------|-------------|
| `data_task1.csv` | Raw dataset (with missing values, duplicates, and inconsistent formats) |
| `task1.py` | Python script used for data cleaning and preprocessing |
| `cleaned_data_task1.csv` | Final cleaned dataset ready for analysis |

---

## 🧠 Objectives
- Identify and handle **missing values**
- Remove **duplicate rows**
- Standardize **text values** (Gender, Country)
- Convert **date formats** into a consistent format
- Ensure all columns have **clean and uniform names**
- Correct **data types** (e.g., age → int, revenue → float, date → datetime)

---

## ⚙️ Steps Performed in `task1.py`

1. **Loaded the dataset** using Pandas  
2. **Handled missing values** using the column mean (`fillna()`)  
3. **Removed duplicates** with `drop_duplicates()`  
4. **Standardized text columns** (converted gender and country values to consistent case)  
5. **Fixed inconsistent date formats** using `pd.to_datetime()`  
6. **Renamed columns** to lowercase and replaced spaces with underscores  
7. **Converted data types** to ensure numeric and datetime consistency  
8. **Saved cleaned data** into a new CSV file  

---

## 📊 Example Output (Cleaned Data)
customerid name gender country age joindate revenue
0 101 John male Usa 25 2023-05-12 4500.0
1 102 Sarah female Usa 30 2023-06-14 3260.0
2 103 John male Canada 28 2023-07-14 3200.0
3 104 Ravi male India 27 2022-03-05 2800.0
4 105 Sarah female Uk 30 2023-06-05 3000.0
5 106 Priya female India 27 2023-03-10 2800.0
