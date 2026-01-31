import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import os
from sqlalchemy import create_engine

# 1. Cargar datos de MySQL
engine = create_engine(f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}")
df = pd.read_sql("SELECT * FROM ecommerce_behavior", engine)

# 2. Preprocesamiento rápido
# Convertimos variables categóricas (mes, tipo de visitante) en números
df_processed = pd.get_dummies(df, columns=['month', 'visitor_type', 'weekend'], drop_first=True)

# 3. Definir X (características) y y (objetivo: revenue)
X = df_processed.drop('revenue', axis=1)
y = df_processed['revenue']

# 4. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Entrenar el modelo de Clasificación
modelo_clasificador = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_clasificador.fit(X_train, y_train)

# 6. Evaluación
predicciones = modelo_clasificador.predict(X_test)

print("--- Informe de Clasificación ---")
print(classification_report(y_test, predicciones))