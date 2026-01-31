import requests

# URL de tu servidor local
URL_VIVIENDA = "http://127.0.0.1:5000/predecir_vivienda"
URL_PROPINA = "http://127.0.0.1:5000/predecir_propina"

# 1. Probando el modelo de VIVIENDAS (Regresión)
print("--- Probando Modelo de Viviendas ---")
casa_nueva = {
    "median_income": 5.5,
    "rooms_per_household": 6.0,
    "population_per_household": 3.0,
    "housing_median_age": 20.0
}

respuesta_v = requests.post(URL_VIVIENDA, json=casa_nueva)
if respuesta_v.status_code == 200:
    print(f"Resultado: {respuesta_v.json()}")
else:
    print("Error en la petición de vivienda")

print("\n" + "-"*30 + "\n")

# 2. Probando el modelo de PROPINAS (Clasificación)
# Nota: Los nombres de columnas deben coincidir con lo que generó pd.get_dummies
print("--- Probando Modelo de Propinas ---")
cliente_nuevo = {
    "total_bill": 50.0,
    "size": 4,
    "sex_Female": 0,
    "smoker_No": 1,
    "day_Fri": 0,
    "day_Sat": 1,
    "day_Sun": 0,
    "time_Dinner": 1
}

respuesta_p = requests.post(URL_PROPINA, json=cliente_nuevo)
if respuesta_p.status_code == 200:
    res = respuesta_p.json()
    estado = "¡Buena propina esperada!" if res['sera_buena_propina'] else "Propina normal."
    print(f"Predicción: {estado}")
    print(f"Probabilidad de éxito: {res['probabilidad_si']}%")
else:
    print("Error en la petición de propina")