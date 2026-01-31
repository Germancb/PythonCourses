import joblib
import pandas as pd
import sys

# 1. Cargar el modelo
nombre_archivo = 'modelo_viviendas_rf.pkl'
try:
    modelo = joblib.load(nombre_archivo)
    print("✅ Sistema listo.")
except:
    print(f"❌ Error: No se encontró '{nombre_archivo}'.")
    sys.exit()

# Lista para guardar el historial de la sesión
historial = []

def solicitar_dato(mensaje):
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada == 's':
            mostrar_resumen_y_salir()
        try:
            return float(entrada)
        except ValueError:
            print("⚠️ Ingresa un número o 's' para salir.")

def mostrar_resumen_y_salir():
    print("\n" + "="*50)
    print("RESUMEN DE LA SESIÓN")
    print("="*50)
    
    if not historial:
        print("No se realizaron consultas.")
    else:
        # Creamos un DataFrame para mostrar el historial como tabla
        df_historial = pd.DataFrame(historial)
        # Renombramos las columnas para que se vean mejor en el resumen
        df_historial.columns = ['Ingreso', 'Habitac.', 'Habitantes', 'Edad', 'Precio Est.']
        print(df_historial.to_string(index=False, float_format=lambda x: f"{x:,.2f}"))
    
    print("\n👋 ¡Gracias por usar el sistema! Saliendo...")
    sys.exit()

# --- BUCLE PRINCIPAL ---
print("\n🏠 BIENVENIDO AL ESTIMADOR DE PRECIOS")
print("(Escribe 's' en cualquier momento para terminar)")

while True:
    print(f"\n--- Consulta #{len(historial) + 1} ---Dar s si ya finalisaste/ Salir del programa")
    
    # Captura de datos
    i = solicitar_dato("1. Ingreso medio (decenas de miles $): ")
    r = solicitar_dato("2. Promedio de habitaciones: ")
    p = solicitar_dato("3. Promedio de habitantes: ")
    e = solicitar_dato("4. Edad de la casa: ")

    # Predicción
    datos = pd.DataFrame([[i, r, p, e]], 
                         columns=['median_income', 'rooms_per_household', 
                                  'population_per_household', 'housing_median_age'])
    
    prediccion = modelo.predict(datos)[0]
    
    # Guardar en historial
    historial.append({
        'ingreso': i, 'rooms': r, 'pop': p, 'age': e, 'precio': prediccion
    })

    print(f"\n💰 VALOR ESTIMADO: ${prediccion:,.2f}")
    print("-" * 30)


    
