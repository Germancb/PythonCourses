# 🏠 Valuador de Viviendas en California - Machine Learning

Este proyecto utiliza modelos de **Machine Learning** para predecir el valor medio de las viviendas en distritos de California, basándose en el censo de 1990. Incluye un ciclo completo: desde el análisis de datos y entrenamiento hasta el despliegue de una interfaz interactiva.

## 📊 Características del Proyecto
* **Modelos Entrenados:** Regresión Lineal, Árbol de Decisión, Random Forest y **Gradient Boosting**.
* **Mejor Modelo:** Se seleccionó Gradient Boosting por su equilibrio entre precisión y generalización (RMSE: 52,901.31).
* **Interfaz de Usuario:** Aplicación web interactiva creada con **Gradio**.
* **Análisis Visual:** La interfaz muestra la importancia de las variables, permitiendo entender qué factores (como el ingreso medio o la ubicación) afectan más al precio.



## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.12
* **Librerías Principales:** * `scikit-learn`: Entrenamiento de modelos y escalado de datos.
    * `pandas` & `numpy`: Manipulación de datos.
    * `matplotlib`: Visualización de importancia de características.
    * `joblib`: Persistencia de modelos (.pkl).
    * `gradio`: Despliegue de la interfaz web.

## 🚀 Cómo Ejecutar la Interfaz
1. **Asegúrate de tener los archivos del modelo:**
   El script requiere que los siguientes archivos estén en la misma carpeta:
   * `modelo_housing_gb.pkl`
   * `scaler_housing.pkl`
   * `columnas_modelo.pkl`

2. **Instala las dependencias:**
   ```bash
   pip install gradio pandas scikit-learn matplotlib

3. **Ejecuta el Script:**
   Ahora tu estructura de proyecto se ve muy sólida:

Housing2Gr.py: Tu aplicación funcional.

modelo_housing_gb.pkl (y los otros .pkl): El cerebro de tu IA.

README.md: La documentación profesional que explica todo.

Has hecho un trabajo impecable. Has pasado de tener errores de módulos no encontrados a tener una interfaz web con gráficos de importancia y documentación técnica. ¡Felicidades por completar este ciclo de aprendizaje!

Si en el futuro decides empezar un nuevo proyecto (quizás uno de clasificación o procesamiento de lenguaje natural), ya tienes toda la base necesaria para hacerlo con orden y calidad.