import joblib
import pandas as pd

# 1. Cargar el modelo guardado
nombre_archivo = 'modelo_viviendas_rf.pkl'

try:
    modelo_cargado = joblib.load(nombre_archivo)
    print(f"--- Modelo '{nombre_archivo}' cargado correctamente ---\n")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {nombre_archivo}. Asegúrate de correr primero el script de entrenamiento.")
    exit()

# 2. Definir nuevos datos para predecir
# Supongamos que tenemos dos casas nuevas con estos datos:
# Columnas: 'median_income', 'rooms_per_household', 'population_per_household', 'housing_median_age'
datos_nuevos = pd.DataFrame([
    [8.32, 6.98, 2.55, 41.0], # Casa 1 (Ingreso alto, antigua)
    [3.12, 4.20, 3.10, 15.0]  # Casa 2 (Ingreso medio-bajo, nueva)
], columns=['median_income', 'rooms_per_household', 'population_per_household', 'housing_median_age'])

# 3. Realizar la predicción
predicciones = modelo_cargado.predict(datos_nuevos)

# 4. Mostrar los resultados de forma elegante
print("Resultados de la estimación:")
for i, precio in enumerate(predicciones):
    print(f" > Vivienda {i+1}: Valor estimado de ${precio:,.2f}")