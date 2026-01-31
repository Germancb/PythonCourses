from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# 1. Cargar los dos modelos
modelo_viviendas = joblib.load('modelo_viviendas_rf.pkl')
modelo_tips = joblib.load('modelo_clasificador_tips.pkl')

@app.route('/predecir_vivienda', methods=['POST'])
def vivienda():
    datos = request.get_json()
    # Usamos DataFrame para mantener consistencia con el entrenamiento
    df_input = pd.DataFrame([datos])
    prediccion = modelo_viviendas.predict(df_input)
    return jsonify({'precio_estimado': float(prediccion[0])})

@app.route('/predecir_propina', methods=['POST'])
def propina():
    datos = request.get_json()
    # Los datos deben incluir total_bill, size y las variables dummies (sex, smoker, etc)
    df_input = pd.DataFrame([datos])
    
    # Asegurarnos de que el orden de columnas sea el mismo que el entrenamiento
    # Para este ejemplo simple, asumimos que el JSON trae las columnas correctas
    resultado = modelo_tips.predict(df_input)
    probabilidad = modelo_tips.predict_proba(df_input)
    
    return jsonify({
        'sera_buena_propina': bool(resultado[0]),
        'probabilidad_si': round(float(probabilidad[0][1]) * 100, 2)
    })
if __name__ == '__main__':
    app.run(debug=True, port=5000)
