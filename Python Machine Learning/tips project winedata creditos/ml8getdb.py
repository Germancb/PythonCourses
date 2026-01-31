import pandas as pd
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

try:
    # 1. Cargar dataset directamente desde la librería Seaborn
    print("Cargando dataset 'tips' desde Seaborn...")
    df = sns.load_dataset('tips')

    # 2. Crear nuestra variable objetivo (Clasificación)
    # ¿La propina es mayor al 15% de la cuenta total?
    df['buena_propina'] = (df['tip'] / df['total_bill'] > 0.15).astype(int)

    # 3. Preparar variables (Convertir texto a números)
    # Convertimos 'sex', 'smoker', 'day', 'time' en columnas numéricas
    df_ml = pd.get_dummies(df.drop(['tip'], axis=1), drop_first=True)

    # 4. Definir X y y
    X = df_ml.drop('buena_propina', axis=1)
    y = df_ml['buena_propina']

    # 5. Entrenar el Clasificador
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo_tips = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo_tips.fit(X_train, y_train)

    # 6. Guardar el modelo
    nombre_archivo = 'modelo_clasificador_tips.pkl'
    joblib.dump(modelo_tips, nombre_archivo)
    
    print("\n--- Reporte de Clasificacion (Propinas) ---")
    print(classification_report(y_test, modelo_tips.predict(X_test)))
    print(f"\nExito: Modelo guardado como {nombre_archivo}")

except Exception as e:
    print(f"Error inesperado: {e}")
