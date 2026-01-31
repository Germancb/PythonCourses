import pandas as pd

cars = pd.read_csv('data.csv')
print(cars.to_string())

ohe_cars = pd.get_dummies(cars[['Car']])
print(ohe_cars.to_string())
# print(ohe_cars)