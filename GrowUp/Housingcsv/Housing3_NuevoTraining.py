import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

# Carga y Limpieza rápida
df = pd.read_csv("Housing.csv")
varlist = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
df[varlist] = df[varlist].apply(lambda x: x.map({'yes': 1, "no": 0}))

# Columnas exactas que usaremos
cols_modelo = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 
               'guestroom', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea']

X = df[cols_modelo]
y = df[['price']]

# Escalamiento (Asegúrate de que X e y se escalen por separado)
sc_X = MinMaxScaler()
sc_y = MinMaxScaler()

X_scaled = sc_X.fit_transform(X)
y_scaled = sc_y.fit_transform(y)

# Entrenamiento
modelo = LinearRegression()
modelo.fit(X_scaled, y_scaled)

# --- VERIFICACIÓN CRÍTICA ---
coeficientes = modelo.coef_.flatten()
print("\n--- PESOS DEL MODELO ---")
for col, coef in zip(cols_modelo, coeficientes):
    print(f"{col}: {coef:.4f}")

# Si los números de arriba son diferentes, ¡estamos listos!
joblib.dump(modelo, 'modelo_housing.pkl')
joblib.dump(sc_X, 'escalador_X.pkl')
joblib.dump(sc_y, 'escalador_y.pkl')
joblib.dump(cols_modelo, 'columnas_seleccionadas.pkl')
print("\n¡Modelo corregido y guardado!")