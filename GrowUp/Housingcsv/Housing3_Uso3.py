import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. CARGA DE DATOS
df = pd.read_csv("Housing.csv")

# 2. PREPROCESAMIENTO BÁSICO
varlist = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
df[varlist] = df[varlist].apply(lambda x: x.map({'yes': 1, "no": 0}))
status = pd.get_dummies(df['furnishingstatus'], drop_first=True)
df = pd.concat([df, status], axis=1)
df.drop(['furnishingstatus'], axis=1, inplace=True)

# 3. DETECCIÓN DE OUTLIERS (Regla del IQR)
Q1 = df.price.quantile(0.25)
Q3 = df.price.quantile(0.75)
IQR = Q3 - Q1
limite_superior = Q3 + 1.5 * IQR

print(f"Límite superior definido: ${limite_superior:,.2f}")

# Creamos dos versiones del dataset
df_normal = df[df.price <= limite_superior]
print(f"Registros originales: {len(df)}")
print(f"Registros tras quitar outliers: {len(df_normal)}")

# 4. FUNCIÓN PARA ENTRENAR Y EVALUAR
def entrenar_modelo(dataset, titulo):
    cols_modelo = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 
                   'guestroom', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea']
    
    X = dataset[cols_modelo]
    y = dataset[['price']]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=100)
    
    scaler_X = MinMaxScaler()
    scaler_y = MinMaxScaler()
    
    X_train_scaled = scaler_X.fit_transform(X_train)
    X_test_scaled = scaler_X.transform(X_test)
    y_train_scaled = scaler_y.fit_transform(y_train)
    y_test_scaled = scaler_y.transform(y_test)
    
    lm = LinearRegression()
    lm.fit(X_train_scaled, y_train_scaled)
    
    preds = lm.predict(X_test_scaled)
    score = r2_score(y_test_scaled, preds)
    
    print(f"R2 Score ({titulo}): {score:.4f}")
    return lm, scaler_X, scaler_y, cols_modelo

# 5. COMPARACIÓN
print("\n--- RESULTADOS ---")
_, _, _, _ = entrenar_modelo(df, "Con Outliers")
modelo_final, sc_X, sc_y, columnas = entrenar_modelo(df_normal, "Sin Outliers (Limpio)")

# 6. GUARDAR EL MODELO LIMPIO (El mejor)
joblib.dump(modelo_final, 'modelo_housing.pkl')
joblib.dump(sc_X, 'escalador_X.pkl')
joblib.dump(sc_y, 'escalador_y.pkl')
joblib.dump(columnas, 'columnas_seleccionadas.pkl')

# 7. VISUALIZACIÓN DE LA MEJORA
plt.figure(figsize=(10,5))
sns.regplot(x='area', y='price', data=df, label='Original (Con Outliers)', scatter_kws={'alpha':0.3})
sns.regplot(x='area', y='price', data=df_normal, label='Limpio (Sin Outliers)', scatter_kws={'alpha':0.5})
plt.title('Efecto de la limpieza de Outliers en la tendencia')
plt.legend()
plt.show()

# # 8plt.figure(figsize=(12, 8))
# Calculamos la correlación solo de las columnas numéricas que usamos
sns.heatmap(df_normal[cols_modelo + ['price']].corr(), annot=True, cmap='RdYlGn', fmt=".2f")
plt.title('Mapa de Correlación: ¿Qué variables se mueven juntas?')
plt.show()