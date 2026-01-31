import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df = pandas.read_csv("data.csv")
x = df[['Weight', 'Volume']]
y = df['CO2']
scaledx = scale.fit_transform(x)
# regresion nuevo vs ml15.py
regr = linear_model.LinearRegression()
regr.fit(scaledx, y)

scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)   # 97.07204485

print(scaled[0][0])   # 4.22105
print(scaled[0][1])     # -4.1973..

slope = regr.coef_
print(slope)
intercept = regr.intercept_ 
print(intercept)
y = slope[0] * scaled[0][0] + slope[1] * scaled[0][1] + intercept
print(y)   # 97.07204485   calculado con a ecuacion y = intercept ' + slope1 * x1 + slope2 * x2 


