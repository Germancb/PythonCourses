import pandas as pd
import sqlite3
import requests
from io import BytesIO

url = "https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"

# 1. Descarga y guardado temporal
response = requests.get(url)
with open("temp_chinook.db", "wb") as f:
    f.write(response.content)

conn = sqlite3.connect("temp_chinook.db")
cursor = conn.cursor()

# 2. LISTAR TODAS LAS TABLAS
print("--- Listado de Tablas en Chinook ---")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

for t in tablas:
    print(f"Tabla encontrada: {t[0]}")

print("-" * 35)

# 3. LEER LA TABLA EMPLOYEE
# Usamos pandas para que se vea ordenado
df_employee = pd.read_sql_query("SELECT * FROM Employee LIMIT 5", conn)
print("\nPrimeras 5 filas de la tabla Employee:")
print(df_employee)

conn.close()