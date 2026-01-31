import pandas as pd
import joblib

def predecir_rf(datos):
    # 1. Cargar el modelo, el escalador y las columnas
    model_rf = joblib.load('modelo_housing_rf.pkl')
    sc = joblib.load('scaler_housing.pkl')
    columnas_entrenamiento = joblib.load('columnas_modelo.pkl')
    
    # 2. Crear DataFrame con el nuevo dato
    df_nuevo = pd.DataFrame([datos])
    
    # 3. Aplicar dummies (esto crea columnas como ocean_proximity_NEAR BAY) [cite: 46]
    df_nuevo = pd.get_dummies(df_nuevo)
    
    # 4. REINDEXAR usando la lista guardada (aquí estaba el error)
    # Esto asegura que el orden y cantidad de columnas sea idéntico al entrenamiento [cite: 74, 80]
    df_nuevo = df_nuevo.reindex(columns=columnas_entrenamiento, fill_value=0)
    
    # 5. Escalar y predecir [cite: 81, 94]
    scaled = sc.transform(df_nuevo)
    return model_rf.predict(scaled)[0]

# Datos de prueba
casa_ejemplo = {
    'longitude': -122.23, 
    'latitude': 37.88, 
    'housing_median_age': 41.0,
    'total_rooms': 880.0, 
    'total_bedrooms': 129.0, 
    'population': 322.0, 
    'households': 126.0, 
    'median_income': 8.3252, 
    'ocean_proximity': 'NEAR BAY'
}

print(f"Predicción RF: ${predecir_rf(casa_ejemplo):,.2f}")