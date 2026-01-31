import gradio as gr
import pandas as pd
import joblib
import matplotlib.pyplot as plt

def predecir_con_grafico(long, lat, age, rooms, bedrooms, pop, households, income, ocean):
    try:
        # 1. Cargar componentes
        modelo = joblib.load('modelo_housing_gb.pkl')
        escalador = joblib.load('scaler_housing.pkl')
        columnas = joblib.load('columnas_modelo.pkl')
        
        # 2. Predicción
        datos = {'longitude': long, 'latitude': lat, 'housing_median_age': age,
                 'total_rooms': rooms, 'total_bedrooms': bedrooms, 'population': pop,
                 'households': households, 'median_income': income, 'ocean_proximity': ocean}
        
        df = pd.DataFrame([datos])
        df = pd.get_dummies(df).reindex(columns=columnas, fill_value=0)
        pred = modelo.predict(escalador.transform(df))[0]
        
        # 3. Crear Gráfico de Importancia
        # plt.close('all') asegura que no se acumulen gráficos en memoria
        plt.close('all')
        fig, ax = plt.subplots(figsize=(8, 4))
        importancias = pd.Series(modelo.feature_importances_, index=columnas).sort_values()
        importancias.plot(kind='barh', ax=ax, color='skyblue')
        ax.set_title("Impacto de cada variable en el precio")
        plt.tight_layout()
        
        return f"Precio Estimado: ${pred:,.2f}", fig

    except Exception as e:
        return f"Error: {e}", None

# Interfaz
app = gr.Interface(
    fn=predecir_con_grafico,
    inputs=[
        gr.Number(label="Longitud", value=-122.24),
        gr.Number(label="Latitud", value=37.85),
        gr.Slider(1, 52, label="Edad casa", value=30),
        gr.Number(label="Habitaciones", value=1500),
        gr.Number(label="Dormitorios", value=300),
        gr.Number(label="Población", value=500),
        gr.Number(label="Hogares", value=200),
        gr.Number(label="Ingreso Medio", value=5.0),
        gr.Dropdown(['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'], label="Zona", value='NEAR BAY')
    ],
    outputs=[
        gr.Textbox(label="Resultado de Predicción"), 
        gr.Plot(label="Gráfico de Importancia de Variables")
    ],
    title="Valuador Housing con Análisis Visual"
)

if __name__ == "__main__":
    # Quitamos el puerto fijo para que Gradio busque el siguiente disponible (7861, 7862, etc.)
    # También quitamos server_name="127.0.0.1" para que use el default por defecto
    app.launch()