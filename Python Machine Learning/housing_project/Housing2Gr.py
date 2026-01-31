import subprocess
import sys
import os

# --- BLOQUE DE AUTO-INSTALACIÓN ---
try:
    import gradio as gr
except ImportError:
    print("Gradio no encontrado. Instalando ahora...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gradio"])
    import gradio as gr
# ----------------------------------

import pandas as pd
import joblib

def predecir_vivienda(long, lat, age, rooms, bedrooms, pop, households, income, ocean):
    try:
        # Cargar los archivos (Deben estar en la misma carpeta que este script)
        modelo = joblib.load('modelo_housing_gb.pkl')
        escalador = joblib.load('scaler_housing.pkl')
        columnas = joblib.load('columnas_modelo.pkl')
        
        datos = {
            'longitude': long, 'latitude': lat, 'housing_median_age': age,
            'total_rooms': rooms, 'total_bedrooms': bedrooms, 'population': pop,
            'households': households, 'median_income': income, 'ocean_proximity': ocean
        }
        
        df_nuevo = pd.DataFrame([datos])
        df_nuevo = pd.get_dummies(df_nuevo).reindex(columns=columnas, fill_value=0)
        df_scaled = escalador.transform(df_nuevo)
        
        pred = modelo.predict(df_scaled)[0]
        return f"Precio Estimado: ${pred:,.2f}"
    
    except Exception as e:
        return f"Error: Verifica que los archivos .pkl existan. Detalle: {e}"

# Interfaz
app = gr.Interface(
    fn=predecir_vivienda,
    inputs=[
        gr.Number(label="Longitud", value=-122.24),
        gr.Number(label="Latitud", value=37.85),
        gr.Slider(1, 52, label="Edad casa", value=52),
        gr.Number(label="Habitaciones", value=1467),
        gr.Number(label="Dormitorios", value=190),
        gr.Number(label="Población", value=496),
        gr.Number(label="Hogares", value=177),
        gr.Number(label="Ingreso Medio", value=7.25),
        gr.Dropdown(['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'], label="Zona", value='NEAR BAY')
    ],
    outputs="text",
    title="Valuador Housing (Gradient Boosting)"
)

import matplotlib.pyplot as plt

# Obtener importancia de las variables del modelo Gradient Boosting
importancias = models['Gradient Boosting'].feature_importances_
columnas = X.columns

# Graficar
plt.figure(figsize=(10,6))
plt.barh(columnas, importancias)
plt.title('¿Qué factores influyen más en el precio?')
plt.show()

if __name__ == "__main__":
# app.launch()
    app.launch(share=False, server_name="0.0.0.0")

