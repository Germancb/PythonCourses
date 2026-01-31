import joblib
import pandas as pd
import sys

# 1. Cargar el modelo
nombre_archivo = 'modelo_viviendas_rf.pkl'
try:
    modelo = joblib.load(nombre_archivo)
    print("✅ Modelo cargado y listo.")
except:
    print(f"❌ Error: No se encontró el archivo '{nombre_archivo}'.")
    sys.exit()

def solicitar_dato(mensaje):
    """Solicita un dato y permite salir si el usuario escribe 's'"""
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada == 's':
            print("\n👋 Cerrando el programa. ¡Hasta luego!")
            sys.exit() # Sale completamente del script
        try:
            return float(entrada)
        except ValueError:
            print("⚠️ Error: Ingresa un número válido o 's' para salir.")

# --- BUCLE PRINCIPAL ---
print("\n" + "="*40)
print("   ESTIMADOR DE PRECIOS DE VIVIENDA")
print("   (Escribe 's' en cualquier momento para salir)")
print("="*40)

while True:
    print("\n--- Nueva consulta --- Entra s si deses salir del programa")
    
    # 2. Captura de datos
    ingreso = solicitar_dato("1. Ingreso medio (decenas de miles $): ")
    habitaciones = solicitar_dato("2. Promedio de habitaciones por hogar: ")
    habitantes = solicitar_dato("3. Promedio de habitantes por hogar: ")
    edad_casa = solicitar_dato("4. Edad media de la vivienda: ")

    # 3. Procesamiento y Predicción
    datos_usuario = pd.DataFrame([[ingreso, habitaciones, habitantes, edad_casa]], 
                                 columns=['median_income', 'rooms_per_household', 
                                          'population_per_household', 'housing_median_age'])
    
    prediccion = modelo.predict(datos_usuario)

    # 4. Resultado
    print("-" * 30)
    print(f"💰 VALOR ESTIMADO: ${prediccion[0]:,.2f}")
    print("-" * 30)
    
    input("\nPresiona ENTER para realizar otra consulta... ")