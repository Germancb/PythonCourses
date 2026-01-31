import numpy as np
import matplotlib.pyplot as plt
# Gráfico de lineas
años = ["2011", "2012", "2013", "2014", "2015",
        "2016", "2017", "2018", "2019", "2020"]

nivel1 = np.random.rand(10)*100
nivel2 = np.random.rand(10)*200 + 100
nivel3 = np.random.rand(10)*300 + 200
nivel4 = np.random.rand(10)*400 + 300
nivel5 = np.random.rand(10)*500 + 400

# Introducir series de datos con color, marcador, etiqueta y estilo

plt.plot(años, nivel1, label="Nivel 1", color="purple", marker="<", linestyle="-")
plt.plot(años, nivel2, label="Nivel 2", color="red", marker="*", linestyle="--")
plt.plot(años, nivel3, label="Nivel 3", color="blue", marker="^", linestyle=":")
plt.plot(años, nivel4, label="Nivel 4", color="black", marker=".", linestyle="-.")
plt.plot(años, nivel5, label="Nivel 5", color="green", marker="+", linestyle=" ")

# Activar leyendas
plt.legend()

# Título de Gráfica
plt.title("Examen de Certificación")

# Etiquetas de los ejes
plt.xlabel("Años que se ha realizado el examen")
plt.ylabel("Puntaje")

# Personalizar Eje de Puntaje de 0 a 1000 en incrementos de 50 

plt.yticks(np.arange(0, 1001, 50))

# Activar cuadrícula 

plt.grid()

# Activar marcas menores
plt.minorticks_on()

plt.show()   # Grafico de lineas con titulo, nombre ejes etc

eje_x = np.arange(0, 10)
# grafic barras verticales
plt.bar(eje_x, nivel5, width=1/5)
plt.bar(eje_x+0.2, nivel4, width=1/5)
plt.bar(eje_x+0.4, nivel3, width=1/5)
plt.bar(eje_x+0.6, nivel2, width=1/5)
plt.bar(eje_x+0.8, nivel1, width=1/5)

plt.show()
# grafico barras horizontakes
plt.barh(eje_x+0.8, nivel5, height = 1/5)
plt.barh(eje_x+0.6, nivel4, height = 1/5)
plt.barh(eje_x+0.4, nivel3, height = 1/5)
plt.barh(eje_x+0.2, nivel2, height = 1/5)
plt.barh(eje_x,     nivel1, height = 1/5)

plt.show()
# grafico barras apliladas
plt.bar(eje_x, nivel5)
plt.bar(eje_x, nivel4, bottom=nivel5)
plt.bar(eje_x, nivel3, bottom=nivel4+nivel5)
plt.bar(eje_x, nivel2, bottom=nivel3+nivel4+nivel5)
plt.bar(eje_x, nivel1, bottom=nivel2+nivel3+nivel4+nivel5)
# grafico dispersion scatter
plt.show()
plt.scatter(eje_x, nivel1, marker="*")
plt.scatter(eje_x, nivel2)
plt.scatter(eje_x, nivel3)
plt.scatter(eje_x, nivel4)
plt.scatter(eje_x, nivel5)

plt.show()
# grafico pastel
plt.pie(nivel1, 
        labels=["México","Colombia", "España", "Estados Unidos", "Ecuador",
                "Argentina", "Venezuela", "Puerto Rico", "Honduras", "Uruguay"])

plt.show()
# Grafico combinado barras, scatter
plt.bar(eje_x,     nivel1,  width = 1/5)
plt.bar(eje_x+0.2, nivel2,  width = 1/5)

plt.plot(años, nivel3)

plt.scatter(eje_x, nivel4)
plt.scatter(eje_x, nivel5)

plt.show()