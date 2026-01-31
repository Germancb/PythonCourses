# Escala normaliza
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing 


datos = pd.read_csv("datos_personas.csv")
print(datos)

# Grafica escala original  Uso de subfiguras  Datos de 1000 personas
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)   # 1 renglon 3 columnas posicion 1  datos originales
ax2 = fig.add_subplot(1, 3, 2)     # pos 2   Ingreso
ax3 = fig.add_subplot(1, 3, 3)       # carros pos 3
ax1.set_title("Datos Originales Juntos")   # lina de abajo imperceptible de 0 a 3
ax1.plot(datos)
ax2.set_title("Ingreso")
ax2.plot(datos["ingreso"], linewidth=0, marker="o", color="blue", markersize=6)   # sin linea t marcadores tamaño
ax3.set_title("Carros")
ax3.plot(datos["carros"], linewidth=0, marker="+", color="orange", markersize=16)  # 0, 1, 2 y 3
plt.show()
 # Distribucion datos originales. Hist histogramas
fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(2, 2, 1)  # 2 renglones , 2 columnas y posicion
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
ax1.set_title("Ingreso")
ax1.plot(datos["ingreso"], linewidth=0, marker="o", color="blue", markersize=6)
ax2.set_title("Carros")
ax2.plot(datos["carros"], linewidth=0, marker="+", color="orange", markersize=16)
ax3.set_title("Ingreso")
ax3.hist(datos["ingreso"], bins=100, color="blue")
ax4.set_title("Carros")
ax4.hist(datos["carros"], color="orange")
plt.show()
# tecnicas Normalización  Tres homgenizadores  min max, Tab, standar robusta prerocesing modulo sklearn
# escala en funcion min max 0 a 1
datos_min_max = preprocessing.MinMaxScaler().fit_transform(datos)
print(datos_min_max)   # arreglos de numpy
# Normaliza en funcion norma vector  datos.T
datos_normalizer = preprocessing.Normalizer().transform(datos.T)   # Trabaja con renglones no con columnnas  T =transpuestas
datos_normalizer = datos_normalizer.T
# normalizado = X / raíz_cuadrada( X_1^2 + X_2^2 + X_3^2 + ...)    Magnitud del vector
print(datos_normalizer)
# Estandariza (desv_std = 1, media = 0)  Standard y Robust
datos_standard_scaler = preprocessing.StandardScaler().fit_transform(datos)
# estandarizado = (X - media) / std

datos_robust_scaler = preprocessing.RobustScaler().fit_transform(datos)
# estandarizado = (X - rango_intercuartílico) / std
print(datos_standard_scaler, datos_robust_scaler)

# Columna ingreso comparacion de metodos
# convierte vectores de numpy a DataFrames para graficarlos
datos_min_max = pd.DataFrame(datos_min_max, columns=["ingreso", "carros"])
datos_normalizer = pd.DataFrame(datos_normalizer, columns=["ingreso", "carros"])
datos_standard_scaler = pd.DataFrame(datos_standard_scaler, columns=["ingreso", "carros"])
datos_robust_scaler = pd.DataFrame(datos_robust_scaler, columns=["ingreso", "carros"])

# crea una figura con 5 subfiguras para comparar los métodos
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)   # 1 renglon 5 columnas
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos
ax1.set_title("INGRESO")
ax1.plot(datos["ingreso"], linewidth=0, marker="*", color="red", markersize=4)

ax2.set_title("Min Max")
ax2.plot(datos_min_max["ingreso"], linewidth=0, marker="*", color="red", markersize=4)

ax3.set_title("Normalizer")
ax3.plot(datos_normalizer["ingreso"], linewidth=0, marker="*", color="red", markersize=4)
#ax3.set_ylim(0, 1)

ax4.set_title("Standard Scaler")
ax4.plot(datos_standard_scaler["ingreso"], linewidth=0, marker="*", color="red", markersize=4)

ax5.set_title("Robust Scaler")
ax5.plot(datos_robust_scaler["ingreso"], linewidth=0, marker="*", color="red", markersize=4)
plt.show()

# crea una figura con 5 subfiguras para mostrar histogramas
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos de los histogramas   Histogramas
ax1.set_title("INGRESO")
ax1.hist(datos["ingreso"], color="red", bins=100)

ax2.set_title("Min Max")
ax2.hist(datos_min_max["ingreso"], color="red", bins=100)

ax3.set_title("Normalizer")
ax3.hist(datos_normalizer["ingreso"], color="red", bins=100)

ax4.set_title("Standard Scaler")
ax4.hist(datos_standard_scaler["ingreso"], color="red", bins=100)

ax5.set_title("Robust Scaler")
ax5.hist(datos_robust_scaler["ingreso"], color="red", bins=100)

plt.show()

# Columna carros comparacion metodos
# crea una figura con 5 subfiguras para comparar los métodos
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos
ax1.set_title("CARROS")
ax1.plot(datos["carros"], linewidth=0, marker="*", color="blue", markersize=4)

ax2.set_title("Min Max")
ax2.plot(datos_min_max["carros"], linewidth=0, marker="*", color="blue", markersize=4)

ax3.set_title("Normalizer")
ax3.plot(datos_normalizer["carros"], linewidth=0, marker="*", color="blue", markersize=4)
ax3.set_ylim(0, 1)

ax4.set_title("Standard Scaler")
ax4.plot(datos_standard_scaler["carros"], linewidth=0, marker="*", color="blue", markersize=4)

ax5.set_title("Robust Scaler")
ax5.plot(datos_robust_scaler["carros"], linewidth=0, marker="*", color="blue", markersize=4)

plt.show()

# crea una figura con 5 subfiguras para mostrar histogramas
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1, 5, 1)
ax2 = fig.add_subplot(1, 5, 2)
ax3 = fig.add_subplot(1, 5, 3)
ax4 = fig.add_subplot(1, 5, 4)
ax5 = fig.add_subplot(1, 5, 5)

# crea y personaliza series de datos de los histogramas
ax1.set_title("CARROS")
ax1.hist(datos["carros"], color="blue")

ax2.set_title("Min Max")
ax2.hist(datos_min_max["carros"], color="blue")

ax3.set_title("Normalizer")
ax3.hist(datos_normalizer["carros"], color="blue")

ax4.set_title("Standard Scaler")
ax4.hist(datos_standard_scaler["carros"], color="blue")

ax5.set_title("Robust Scaler")
ax5.hist(datos_robust_scaler["carros"], color="blue")

plt.show()