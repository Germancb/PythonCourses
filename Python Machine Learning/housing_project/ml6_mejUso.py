import streamlit as st
import joblib
import pandas as pd

# Cargar el nuevo modelo
modelo = joblib.load('modelo_viviendas_geo.pkl')

st.title("📍 Predicción Inmobiliaria Geográfica")

# Sidebar
st.sidebar.header("Ubicación y Datos")
# Rangos reales de California
lat = st.sidebar.slider("Latitud", 32.5, 42.0, 37.8)
lon = st.sidebar.slider("Longitud", -124.3, -114.3, -122.2)
ingreso = st.sidebar.slider("Ingreso Medio", 0.5, 15.0, 4.0)
rooms = st.sidebar.slider("Habitaciones", 1.0, 10.0, 5.0)
edad = st.sidebar.slider("Edad Casa", 1, 52, 30)

# Predicción
input_df = pd.DataFrame([[lon, lat, ingreso, rooms, edad]], 
                        columns=['longitude', 'latitude', 'median_income', 'rooms_per_household', 'housing_median_age'])
prediccion = modelo.predict(input_df)[0]

# Resultados
col1, col2 = st.columns(2)
with col1:
    st.metric("Precio Estimado", f"${prediccion:,.2f}")
    
with col2:
    # Mostrar el punto exacto en el mapa
    punto_mapa = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(punto_mapa, zoom=5)

st.write(f"Coordenadas actuales: {lat}, {lon}")

    
