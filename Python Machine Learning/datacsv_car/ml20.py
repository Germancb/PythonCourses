import pandas
import sys
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("data2.csv")
print(df.head())

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
print(X)
print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
tree.plot_tree(dtree, feature_names=features) 
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()  # aparecen símbolos

print("ojo")
print(dtree.predict([[40, 10, 7, 1]]))

# Example  What would the answer be if the comedy rank was 6?
print(dtree.predict([[40, 10, 6, 1]]))
