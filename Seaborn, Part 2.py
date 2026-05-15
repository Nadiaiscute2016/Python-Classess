import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("your_dataset.csv")
sns.pairplot(data)
plt.show()
sns.heatmap(data.corr(), annot=True)
plt.show()