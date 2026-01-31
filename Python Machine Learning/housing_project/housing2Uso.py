# uso Modeo regresion grabado en Housing2.ipynb
import joblib
import pandas as pd

# Cargar el modelo y el escalador
modelo_cargado = joblib.load('modelo_housing_lr.pkl')
scaler_cargado = joblib.load('scaler_housing.pkl')

# Ejemplo: Datos de una nueva vivienda para predecir
# Asegúrate de que los nombres de las columnas coincidan con el entrenamiento
nuevos_datos = pd.DataFrame([{
    'longitude': -122.23,
    'latitude': 37.88,
    'housing_median_age': 41.0,
    'total_rooms': 880.0,
    'total_bedrooms': 129.0,
    'population': 322.0,
    'households': 126.0,
    'median_income': 8.32,
    'ocean_proximity_<1H OCEAN': 0,
    'ocean_proximity_INLAND': 0,
    'ocean_proximity_ISLAND': 0,
    'ocean_proximity_NEAR BAY': 1,
    'ocean_proximity_NEAR OCEAN': 0
}])

# 1. Escalar los nuevos datos
nuevos_datos_scaled = scaler_cargado.transform(nuevos_datos)

# 2. Realizar la predicción
prediccion = modelo_cargado.predict(nuevos_datos_scaled)

print(f"El valor predicho para la vivienda es: ${prediccion[0]:,.2f}")