#TASK 1: Data loading and exploration steps.
import pandas as pd
import numpy as np

df = pd.read_csv('winequality-red.csv', 'winequality-white.csv', 'winequality.names')

df.head()
df.info()
df.isnull().sum()

df_filled = df.fillna(df.mean(numeric_only=True))
df_dropped = df.dropna()
df = df_filled


#TASK 2: Basic data analysis results.
print(df.describe())

# Group by 'quality' and compute mean for each group
group_means = df.groupby('quality').mean(numeric_only=True)
print(group_means)

print(group_means['alcohol'])


#TASK 3: Visualizations.
import matplotlib.pyplot as plt
import seaborn as sns

# Line chart of average alcohol by wine quality
plt.figure(figsize=(8,5))
plt.plot(group_means.index, group_means['alcohol'], marker='o')
plt.title('Average Alcohol Content by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Average Alcohol')
plt.grid(True)
plt.show()

# Bar chart: average alcohol per quality
group_means['alcohol'].plot(kind='bar', color='skyblue')
plt.title('Average Alcohol Content by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Average Alcohol')
plt.show()

plt.hist(df['alcohol'], bins=20, color='orange', edgecolor='black')
plt.title('Distribution of Alcohol Content')
plt.xlabel('Alcohol')
plt.ylabel('Frequency')
plt.show()

#Scatter Plot: alcohol vs quality
plt.scatter(df['alcohol'], df['quality'], alpha=0.5)
plt.title('Alcohol Content vs. Wine Quality')
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.show()


#TASK 4: Any findings or observations.
# 1. The average alcohol content tends to increase with wine quality, as seen in both the group means and the line/bar charts.
# 2. The histogram shows that most wines have an alcohol content between X and Y percent.
# 3. The scatter plot suggests a weak/moderate/strong correlation between alcohol content and wine quality.
# 4. There are no missing values after cleaning, so the dataset is complete for analysis.