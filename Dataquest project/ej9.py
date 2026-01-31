#%% Celda 1: Hola Mundo
print("Hola desde la celda 1")

#%% Celda 2: Operaciones básicas
a = 10
b = 20
print("Suma:", a + b)
print("Multiplicación:", a * b)

#%% Celda 3: Datos y gráfico
import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = {"Edad": [22, 25, 25, 30, 32, 32, 35, 40, 40, 45]}
df = pd.DataFrame(data)

print("Primeras filas del DataFrame:")
print(df.head())

# Histograma
df["Edad"].hist(bins=5, edgecolor="black", color="skyblue")
plt.title("Histograma de Edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()

# %%
