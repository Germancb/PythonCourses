
# Ejemplo: Datos de viviendas de California (muy usado en ML)
import pandas as pd
import sqlite3

# 1. Cargamos el CSV desde la web
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
df = pd.read_csv(url)
# print(df.head())
# 2. Creamos una base de datos SQLite en memoria (o en un archivo)
conn = sqlite3.connect('mi_base_de_datos.db')

# 3. Guardamos el DataFrame como una tabla llamada 'california'
df.to_sql('california', conn, if_exists='replace', index=False)

# 4. AHORA SÍ: Consultamos la lista de tablas existentes
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

print("Tablas encontradas en la DB:")
for t in tablas:
    print(f"- {t[0]}")

conn.close()
print(df.head())

# Solo tien un Data frame: df_housing


