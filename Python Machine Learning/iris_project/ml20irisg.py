import pandas
import matplotlib.pyplot as plt
import seaborn as sns

fileurl = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal_length','sepal_width','petal_length','petal_width','class']
data = pandas.read_csv(fileurl, names=names)

#Print the correlation
pandas.set_option('display.width', 100)
# pandas.set_option('precision', 2)
# correlations = data.corr(method='pearson')
correlations = data.corr(numeric_only=True)
print(correlations)

# corr = df.corr()
# plot the heat map
fig, ax = plt.subplots(figsize=(5,4))
sns.heatmap(correlations, annot=True, ax=ax, cmap = 'coolwarm')
plt.show()
#-1 indicates 100% negative correlation,
# indicates 100% correlation. 0 Indicates no correlation.