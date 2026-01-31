# 🏠 Estimador de Precios de Vivienda con IA

Este proyecto utiliza un modelo de **Regresión Lineal** para predecir el valor de mercado de propiedades residenciales. Incluye una interfaz web interactiva construida con **Streamlit**.

## 📊 Características del Proyecto
- **Limpieza de Outliers:** Eliminación de valores atípicos mediante el método IQR para mejorar la precisión.
- **Normalización:** Uso de `MinMaxScaler` para equilibrar el peso de todas las variables.
- **Visualización:** Gráficos de importancia de variables en tiempo real.

## 🛠️ Tecnologías utilizadas
- **Python 3.10+**
- **Scikit-Learn** (Modelado y Preprocesamiento)
- **Pandas & Numpy** (Manipulación de datos)
- **Streamlit** (Interfaz Web)

## 🚀 Cómo ejecutarlo localmente
1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta la app: `streamlit run Housing_Web.py`

## 📈 Insights del Modelo
Según el entrenamiento, los factores más influyentes en el precio son:
1. **Área Total**
2. **Número de Baños**
3. **Pisos (Stories)**