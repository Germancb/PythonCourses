import pandas as pd
from sqlalchemy import create_engine

# Configuración manual
user = 'root'
passw = 'Gerco&9371' # <-- CAMBIA ESTO
host = 'localhost'
db = 'chinook'

# Creación del motor
engine = create_engine(f"mysql+mysqlconnector://{user}:{passw}@{host}/{db}")

# Prueba de conexión y carga de datos
try:
    # Una consulta simple para probar que funciona
    query = "SELECT * FROM customers LIMIT 5" 
    df = pd.read_sql(query, engine)
    print("¡Conectado con éxito!")
    print(df)
except Exception as e:
    print(f"No se pudo conectar. El error es: {e}")