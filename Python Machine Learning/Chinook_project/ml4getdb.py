import pandas as pd
import sqlite3
import requests
from io import BytesIO

url = "https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"

# Descargar el contenido del archivo
response = requests.get(url)
# Crear una conexión a la base de datos en memoria a partir de los bytes descargados
db = BytesIO(response.content)

# Para archivos SQLite remotos, a veces es más fácil guardarlo un segundo:
with open("temp_chinook.db", "wb") as f:
    f.write(response.content)

conn = sqlite3.connect("temp_chinook.db")
cursor = conn.cursor()
tables = cursor.fetchall()

# Print the table names
# Execute the SQL query to select table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
df = pd.read_sql_query("SELECT * FROM Customer LIMIT 5", conn)  # Customer
print(df)