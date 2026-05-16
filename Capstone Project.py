import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Age': [25, 30, 35, np.nan, 40, 45, 50, 55, 60, 65],
    'Salary': [50000, 60000, 65000, 70000, np.nan, 80000, 85000, 90000, 95000, 100000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR', 'Marketing', 'IT', 'HR', 'Marketing', 'IT'],
    'Performance_Score': [4.2, 3.8, 4.5, 3.9, 4.1, 4.7, 3.6, 4.0, 4.4, 4.8]
}
df = pd.DataFrame(data)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['Salary_Per_Year_Of_Age'] = df['Salary'] / df['Age']
high_performers = df[df['Performance_Score'] > 4.0]
summary_stats = df.groupby('Department')['Salary'].agg(['mean', 'median', 'std'])
correlation_matrix = df[['Age', 'Salary', 'Performance_Score']].corr()
np_salaries = df['Salary'].to_numpy()
normalized_salaries = (np_salaries - np.mean(np_salaries)) / np.std(np_salaries)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Age', y='Salary', hue='Department', s=100)
plt.title('Salary vs Age by Department')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Department', y='Performance_Score', errorbar=None)
plt.title('Average Performance Score by Department')
plt.xlabel('Department')
plt.ylabel('Average Performance')
plt.tight_layout()
plt.show()
plt.figure(figsize=(6, 5))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()