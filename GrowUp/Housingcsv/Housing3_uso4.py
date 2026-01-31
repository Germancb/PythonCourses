

import streamlit as st
import joblib
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Estimador Inmobiliario AI", page_icon="🏠")

# 1. Cargar el cerebro de la App
@st.cache_resource # Esto hace que la app sea ultra rápida
def cargar_componentes():
    modelo = joblib.load('modelo_housing.pkl')
    sc_X = joblib.load('escalador_X.pkl')
    sc_y = joblib.load('escalador_y.pkl')
    columnas = joblib.load('columnas_seleccionadas.pkl')
    return modelo, sc_X, sc_y, columnas

modelo, sc_X, sc_y, columnas = cargar_componentes()

# 2. Interfaz de Usuario
st.title("🏠 Inteligencia Artificial Inmobiliaria")
st.markdown("Ajusta las características para calcular el valor de mercado de la propiedad.")

with st.sidebar:
    st.header("Características Técnicas")
    area = st.slider("Área total (sqft)", 1000, 15000, 5000)
    bedrooms = st.number_input("Habitaciones", 1, 6, 3)
    bathrooms = st.number_input("Baños", 1, 4, 2)
    stories = st.selectbox("Pisos", [1, 2, 3, 4])
    parking = st.slider("Espacios de Parking", 0, 3, 1)

st.subheader("Extras y Amenidades")
col1, col2 = st.columns(2)

with col1:
    mainroad = st.checkbox("Acceso a vía principal")
    guestroom = st.checkbox("Cuarto de huéspedes")
    hotwater = st.checkbox("Calentador de agua")

with col2:
    aircon = st.checkbox("Aire Acondicionado")
    prefarea = st.checkbox("Zona Preferencial")

# 3. Procesamiento de datos
datos = {
    'area': area, 'bedrooms': bedrooms, 'bathrooms': bathrooms,
    'stories': stories, 'mainroad': 1 if mainroad else 0,
    'guestroom': 1 if guestroom else 0, 'hotwaterheating': 1 if hotwater else 0,
    'airconditioning': 1 if aircon else 0, 'parking': parking,
    'prefarea': 1 if prefarea else 0
}

# 4. Predicción
if st.button("Calcular Precio Estimado"):
    df_entrada = pd.DataFrame([datos])[columnas]
    X_scaled = sc_X.transform(df_entrada)
    pred_decimal = modelo.predict(X_scaled)
    precio_final = sc_y.inverse_transform(pred_decimal.reshape(-1, 1))[0][0]
    
    st.success(f"### El valor estimado es: ${precio_final:,.2f}")
    st.balloons() # ¡Celebración de éxito!

# ... (debajo de la parte donde calculas el precio_final)

st.divider() # Una línea divisoria estética

st.subheader("📊 Análisis de Valor: ¿Qué influye más en este precio?")

# 1. Extraer los coeficientes del modelo (importancia)
importancias = modelo.coef_[0]

# 2. Crear un DataFrame para la gráfica
df_importancia = pd.DataFrame({
    'Atributo': columnas,
    'Impacto': importancias
}).sort_values(by='Impacto', ascending=False)

# 3. Mostrar la gráfica de barras
st.bar_chart(df_importancia.set_index('Atributo'))

st.info("""
**Nota:** Las barras más altas indican las variables que más aumentan el valor de la propiedad 
según el modelo de Regresión Lineal entrenado.
""")