
# Ejemplo: Datos de viviendas de California (muy usado en ML)
import pandas as pd
import sqlite3
import requests
from io import BytesIO

url_datos = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

df_housing = pd.read_csv(url_datos)
print("Dataset de ML leído directamente de URL:")
print(df_housing.head())
# Solo tien un Data frame: df_housing


