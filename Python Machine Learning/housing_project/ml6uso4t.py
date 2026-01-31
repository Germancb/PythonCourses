# Solo corre si en VS code en PS C:\Users\ACER\PYTHON COURSES\Python Machine Learning\housing project> streamlit run ml6uso4t.py
# streamlit run ml6uso4t.py    OJO al streamlit NO->no  py ml6uso4t.py   OJO
# Esto abrirá automáticamente una pestaña en tu navegador 
# (normalmente en http://localhost:8501).
import streamlit as st
import joblib
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Estimador de Viviendas", page_icon="🏠")

# 1. Cargar el modelo
@st.cache_resource # Esto evita que el modelo se recargue cada vez que mueves un control
def cargar_modelo():
    return joblib.load('modelo_viviendas_rf.pkl')

modelo = cargar_modelo()

# 2. Interfaz de usuario
st.title("🏠 Predicción de Precios de Vivienda")
st.markdown("Mueve los controles para ver cómo cambia el valor estimado en tiempo real.")

# Sidebar (Barra lateral) para los datos de entrada
st.sidebar.header("Parámetros de la Vivienda")

ingreso = st.sidebar.slider("Ingreso medio (decenas de miles $)", 0.5, 15.0, 3.5)
habitaciones = st.sidebar.slider("Habitaciones por hogar", 1.0, 10.0, 5.0)
habitantes = st.sidebar.slider("Habitantes por hogar", 1.0, 10.0, 3.0)
edad = st.sidebar.slider("Edad media de la casa", 1, 52, 25)

# 3. Preparar datos y predecir
datos_entrada = pd.DataFrame([[ingreso, habitaciones, habitantes, edad]], 
                             columns=['median_income', 'rooms_per_household', 
                                      'population_per_household', 'housing_median_age'])

prediccion = modelo.predict(datos_entrada)[0]

# 4. Mostrar resultado con estilo
st.subheader("Valor Estimado de la Propiedad:")
st.success(f"### ${prediccion:,.2f} USD")

# Comparativa rápida
st.info(f"Con un ingreso de **${ingreso*10:,.0f} USD**, el modelo estima este valor.")


    
