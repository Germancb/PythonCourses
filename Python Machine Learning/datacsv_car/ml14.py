import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")
x = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x, y)
slope = regr.coef_
print(slope)
intercept = regr.intercept_ 
print(intercept)
y = slope[0] * 2300 + slope[1] * 1300 + intercept
print(y)
#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)  # 107.2087328

# print(regr.coef_)  # # #[114.75968007]

# predictedCO2 = regr.predict([[3300, 1300]])
# print(predictedCO2)  #[0.00755095 0.00780526]