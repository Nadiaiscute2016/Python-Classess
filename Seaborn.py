import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
print(df.head())
sns.boxplot(data=df, x="day", y="total_bill")
plt.title("Bill Distribution by Day")
plt.show()
sns.histplot(df['total_bill'], kde=True)
plt.title("Distribution of Total Bills")
plt.show()