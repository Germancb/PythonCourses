#%% Importar librerías
import pandas as pd
import matplotlib.pyplot as plt

#%% Cargar datos
star_wars = pd.read_csv("StarWars.csv", encoding="ISO-8859-1")
print(star_wars.head())

star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")
#%% Cargar datos
star_wars = pd.read_csv("StarWars.csv", encoding="ISO-8859-1")
print(star_wars.info())

#%% Ver estructura básica
print("Tamaño del dataset:", star_wars.shape)   # filas y columnas
print("Columnas:", star_wars.columns.tolist())  # nombres de columnas

#%% Ver primeras filas
print(star_wars.head())

#%% Ejemplo: Histograma de una columna numérica (ajusta el nombre de la columna si existe)
if "Age" in star_wars.columns:
    star_wars["Age"].hist(bins=10, edgecolor="black", color="skyblue")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de edades - Encuesta Star Wars")
    plt.show()
else:
    print("No existe la columna 'Age' en este dataset.")
