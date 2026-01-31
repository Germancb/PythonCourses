# importing packages
import seaborn as sns # Cmparing etal length petal width
import matplotlib.pyplot as plt

import pandas as pd

# Reading the CSV file
df = pd.read_csv("Iris.csv")

# Printing top 5 rows
df.head()
sns.countplot(x='Species', data=df, )
plt.show()

sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm',
                hue='Species', data=df, )

# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=2)

plt.show()