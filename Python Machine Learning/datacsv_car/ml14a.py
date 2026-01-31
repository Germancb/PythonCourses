import pandas
from sklearn import linear_model
df = pandas.read_csv("data2.csv")
print(df.head())
print(df.tail())
desc1 = df.describe()
print(desc1)
x = df[['Age', 'Experience']]
# x = df[['Age']]
y = df['Rank']

regr = linear_model.LinearRegression()
regr.fit(x, y)

#predict Rank age 40, experience 10 years

predictedRank = regr.predict([[40.0, 15.2]])
print(predictedRank) 