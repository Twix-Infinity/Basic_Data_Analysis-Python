#TASK 1: Data loading and exploration steps.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_excel('Book1.xlsx')
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

print("Column names:", df.columns.tolist())
print(df.head())

# Explore the structure
print(df.info())
print(df.isnull().sum())

# Clean the dataset by filling missing values
df = df.fillna(df.mean(numeric_only=True))

# Ensure 'Grade' is numeric
if 'Grade' in df.columns:
    df['Grade'] = pd.to_numeric(df['Grade'], errors='coerce')

# Check if DataFrame is empty after cleaning
if df.empty:
    print("DataFrame is empty after cleaning. Exiting.")
    exit()

print("Median of numerical columns:")
print(df.median(numeric_only=True))

#TASK 2: Basic data analysis results.
print(df.describe())

# Group by 'Class Stream' and compute mean for each class
if 'ClassStream' in df.columns and 'Grade' in df.columns:
    group_means = df.groupby('ClassStream').mean(numeric_only=True)
    print(group_means)
    print(group_means['Grade'])
else:
    print("Required columns 'ClassStream' and/or 'Grade' not found in the dataset.")

#TASK 3: Visualizations.
if 'Class Stream' in df.columns and 'Grade' in df.columns:
    # Line chart of average grade by class stream
    plt.figure(figsize=(8,5))
    plt.plot(group_means.index, group_means['Grade'], marker='o')
    plt.title('Average Student Grade by Class Stream')
    plt.xlabel('Class Stream')
    plt.ylabel('Average Grade')
    plt.grid(True)
    plt.show()

    # Bar chart: average grade per class stream
    sns.barplot(x=group_means.index, y=group_means['Grade'])
    plt.title('Average Student Grade by Class Stream')
    plt.xlabel('Class Stream')
    plt.ylabel('Average Grade')
    plt.show()

    # Histogram chart of grades
    plt.hist(df['Grade'], bins=20, color='orange', edgecolor='black')
    plt.title('Distribution of Student Grades')
    plt.xlabel('Grade')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("Skipping class stream/grade visualizations due to missing columns.")

# Scatter Plot: grade vs. previous grade
num_cols = df.select_dtypes(include=np.number).columns.tolist()
other_num_cols = [col for col in num_cols if col != 'Grade']

# Scatter plot: Grade vs. Previous Grade (if both exist)
if 'Grade' in df.columns and 'Previous Grade' in df.columns:
    plt.scatter(df['Grade'], df['Previous Grade'], alpha=0.5)
    plt.title('Grade vs. Previous Grade')
    plt.xlabel('Grade')
    plt.ylabel('Previous Grade')
    plt.show()

# Scatter plots: Grade vs. all other numerical columns except 'Previous Grade'
if 'Grade' in df.columns and other_num_cols:
    for col in other_num_cols:
        if col != 'Previous Grade':
            plt.scatter(df['Grade'], df[col], alpha=0.5)
            plt.title(f'Grade vs. {col}')
            plt.xlabel('Grade')
            plt.ylabel(col)
            plt.show()
elif not other_num_cols:
    print("No suitable numerical columns found for scatter plot.")

#TASK 4: Any findings or observations.
# 1. The average grade varies by class stream, as seen in the group means and the line/bar charts.
# 2. The histogram shows the distribution of student grades.
# 3. The scatter plot (if applicable) shows the relationship between student grades and another numerical column.
# 4. There are no missing values after cleaning, so the dataset is complete for analysis.