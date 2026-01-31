import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 1. Cargar los datos (usando el DataFrame que ya tienes de la web)
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
df = pd.read_csv(url)
print(df.head())
# 2. FEATURE ENGINEERING: Creamos columnas más inteligentes
df["rooms_per_household"] = df["total_rooms"] / df["households"]
df["population_per_household"] = df["population"] / df["households"]

# 3. Limpieza: Llenamos nulos para que el modelo no falle
df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())

# 4. Seleccionamos las nuevas variables + las mejores anteriores
features = ['median_income', 'rooms_per_household', 'population_per_household', 'housing_median_age']
X = df[features]
y = df['median_house_value']

# 5. Dividir y Entrenar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo_final = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_final.fit(X_train, y_train)

# 6. Evaluación
error = mean_absolute_error(y_test, modelo_final.predict(X_test))
print(f"Nuevo Error promedio (MAE) con variables optimizadas: ${error:,.2f}")

import joblib

# 1. Definir el nombre del archivo (Viviendas es REGRESIÓN, no clasificación)
nombre_archivo = 'modelo_viviendas_rf.pkl'

try:
    # 2. Guardar el modelo que acabas de entrenar (modelo_final)
    joblib.dump(modelo_final, nombre_archivo)
    print(f"Modelo guardado exitosamente como: {nombre_archivo}")
    
except NameError:
    print("Error: La variable 'modelo_final' no existe. Revisa el nombre del modelo entrenado arriba.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")