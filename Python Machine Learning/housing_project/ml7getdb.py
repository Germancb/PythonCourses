
import joblib
import pandas as pd

# 1. Cargar el modelo
nombre_archivo = 'modelo_viviendas_rf.pkl'
modelo_cargado = joblib.load(nombre_archivo)

# 2. Definir los datos nuevos
columnas = ['median_income', 'rooms_per_household', 'population_per_household', 'housing_median_age']
datos_nuevos = pd.DataFrame([[4.5, 6.2, 2.8, 35]], columns=columnas)

# 3. Predecir
prediccion = modelo_cargado.predict(datos_nuevos)

# 4. Imprimir el resultado (SIN EMOJIS para evitar el error de Unicode)
print("--- Resultado de la Prediccion ---")
print(f"El valor estimado de la propiedad es: ${prediccion[0]:,.2f}")