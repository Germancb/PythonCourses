import pandas as pd
# import matplotlib as plt
import matplotlib.pyplot as plt
# Quitar notacion cientifica
pd.options.display.float_format = '{:2f}'.format
# contexto
# [0] edad
# (1) Gastos mes medicina
# (2) gastos mes educacion
# (3) Gastos mes cacahuates
datos = {"edad":[35, 50, 22, 45, 18, 75, 55, 20, 23, 49],
         "medicina":[200, 1500, 150, 250, 0, 2500, 1400, 50, 0, 600],
         "educacion":[1200, 0, 7500, 2200, 8300, 0, 0, 4900, 5100, 800],
         "cacahuetes":[10, 15, 0, 10, 20, 10, 20, 10, 15, 0]}
datos = pd.DataFrame(datos)
print(datos)
print(datos.std())
print(datos.aggregate(["std", "var"]))

def subgrafica_std(datos, columna,   fig, posicion):
    ax = fig.add_subplot(1, 4, posicion)
# calculo media y desv st
    media = datos[columna].mean()   
    std = datos[columna].std()
# graficando datos
    print(media, std) 
    # ax.scatter(range(len(datos[columna])), datos[columna], marker="0", s=150, color="purple")   
    ax.scatter(range(len(datos[columna])), datos[columna], s=150, color="purple") 

    ax.axhline(y=media+std, color="gray", linestyle="--", linewidth=3)
    ax.axhline(y=media, color="teal", linestyle=":", linewidth=6)
    ax.axhline(y=media-std, color="gray", linestyle="--", linewidth=3)
    # ax.scatter(data.x, data.y, c='b', zorder=2)

    ax.set_title("Dev std: " + columna.capitalize(), fontsize=20)
    ax.set_xticks(range(len(datos[columna])))
    ax.get_xaxis().set_visible(False)

# desv sta d para todas las columnas
fig = plt.figure(figsize=(18, 5))

subgrafica_std(datos, "edad", fig, 1)
subgrafica_std(datos, "medicina", fig, 2)
subgrafica_std(datos, "educacion", fig, 3)
subgrafica_std(datos, "cacahuetes", fig, 4)

plt.show()
print(datos.var())
print(datos.cov())

def subgrafica_dispersion(datos, col_a, col_b, fig, posicion, texto):
    ax = fig.add_subplot(1, 3, posicion)
    # ax.scatter(range(len(datos[columna])), datos[columna], marker="0", s=150, color="purple")   
    ax.scatter(datos[col_a], datos[col_b], marker = 8, s=250, color="purple")

    ax.set_xlabel(col_a.capitalize(), fontsize=20, color="darkblue")
    ax.set_ylabel(col_b.capitalize(), fontsize=20, color="darkblue")
    ax.text(54, 8, texto, fontsize=20, color="darkblue")

# impresin matrices covarianza
print(datos[["edad", "medicina"]].cov(),  "\n")
print(datos[["edad", "educacion"]].cov(),  "\n")
print(datos[["edad", "cacahuetes"]].cov(),  "\n")

#Graficos
fig = plt.figure(figsize=(20, 6))
subgrafica_dispersion(datos, "edad", "medicina", fig, 1, "Positiva")
subgrafica_dispersion(datos, "edad", "educacion", fig, 2, "Negativa")
subgrafica_dispersion(datos, "edad", "cacahuetes", fig, 3, "~Cero")

plt.show()
# print(datos.var())
# print(datos.cov())