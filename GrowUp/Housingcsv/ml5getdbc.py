
# Ejemplo: Datos de viviendas de California (muy usado en ML)
import pandas as pd
from sklearn import linear_model
import sqlite3

df = pandas.read_csv("Housing.csv")
print(df.head())
print(df.tail())