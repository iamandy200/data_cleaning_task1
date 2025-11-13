import pandas as pd

#load the data set
df = pd.read_csv(r"C:\Users\Lenovo\Downloads\data_task1.csv")
print('original data:')
print(df)

#handle missing values
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Revenue'].fillna(df['Revenue'].mean(),inplace=True)

#Remove duplicates
before_dup = df.shape[0]
df.drop_duplicates(inplace=True)
after_dup = df.shape[0]

#Standardize text columns
df['Gender']=df['Gender'].str.lower().str.strip()
df['Country']=df['Country'].str.title().str.strip()

#Fix inconsistent date formats properly
# Replace all date separators (/, ., etc.) with '-'
df['JoinDate'] = df['JoinDate'].astype(str).str.replace(r"[./]", "-", regex=True)

# Convert to datetime with dayfirst=True for formats like 14-07-23
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce', dayfirst=True)

# Optional: Fill remaining NaT values with the most common date
df['JoinDate'].fillna(df['JoinDate'].mode()[0], inplace=True)

#Rename columns to clean format
df.columns = df.columns.str.lower().str.replace(' ', '_')

#Convert datatypes
df['age'] = df['age'].astype(int)
df['revenue'] = df['revenue'].astype(float)

#Display cleaned data
print("\n✅ Cleaned Data:")
print(df)

#Summary of cleaning
print("\n📊 Data Cleaning Summary:")
print(f"→ Missing 'Age' filled with mean: {df['age'].mean():.2f}")
print(f"→ Missing 'Revenue' filled with mean: {df['revenue'].mean():.2f}")
print(f"→ Duplicates removed: {before_dup - after_dup}")
print(f"→ Total rows after cleaning: {df.shape[0]}")
print(f"→ Null values remaining:\n{df.isnull().sum()}")

