import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# 1. Carga de datos
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
df = pd.read_csv(url)

# 2. Limpieza y Feature Engineering
df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())
df["rooms_per_household"] = df["total_rooms"] / df["households"]

# 3. Seleccionamos Latitud y Longitud como variables CLAVE
features = ['longitude', 'latitude', 'median_income', 'rooms_per_household', 'housing_median_age']
X = df[features]
y = df['median_house_value']

# 4. Entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo_geo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo_geo.fit(X_train, y_train)

# 5. Guardar el nuevo modelo
joblib.dump(modelo_geo, 'modelo_viviendas_geo.pkl')
print("✅ Nuevo modelo guardado como 'modelo_viviendas_geo.pkl' con datos geográficos.")

    
