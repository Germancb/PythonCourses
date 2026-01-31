import pandas

fileurl = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal_length','sepal_width','petal_length','petal_width','class']
data = pandas.read_csv(fileurl, names=names)

print(data.head())