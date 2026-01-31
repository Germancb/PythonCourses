import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Configuración y Carga
st.set_page_config(layout="wide", page_title="Housing Analyzer")
modelo = joblib.load('modelo_viviendas_rf.pkl')

# 2. Interfaz Lateral
st.sidebar.header("⚙️ Configuración de la Casa")
ingreso = st.sidebar.slider("Ingreso (Decenas de mil $)", 0.5, 15.0, 3.8)
habitaciones = st.sidebar.slider("Habitaciones promedio", 1.0, 10.0, 5.2)
habitantes = st.sidebar.slider("Habitantes promedio", 1.0, 8.0, 3.0)
edad = st.sidebar.slider("Edad de la vivienda", 1, 52, 28)

# 3. Predicción
datos = pd.DataFrame([[ingreso, habitaciones, habitantes, edad]], 
                     columns=['median_income', 'rooms_per_household', 
                              'population_per_household', 'housing_median_age'])
precio_predicho = modelo.predict(datos)[0]

# 4. Diseño de la Página Principal
st.title("📊 Análisis Predictivo de Viviendas")

col1, col2 = st.columns([1, 1])

with col1:
    st.metric(label="Precio Estimado", value=f"${precio_predicho:,.2f}")
    st.write("Este valor se calcula mediante un bosque de 100 árboles de decisión.")

with col2:
    # Gráfico comparativo simple
    precios_referencia = pd.DataFrame({
        'Categoría': ['Tu Predicción', 'Promedio California'],
        'Precio ($)': [precio_predicho, 206855] # 206k es el promedio real del dataset
    })
    st.bar_chart(data=precios_referencia, x='Categoría', y='Precio ($)')

# 5. Sección de Mapa (California)
st.subheader("📍 Ubicación del Dataset")
st.write("El modelo fue entrenado con datos geográficos de California:")
# Generamos unos puntos aleatorios en el rango de California para ilustrar el mapa
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [20, 20] + [37.7, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)


    
