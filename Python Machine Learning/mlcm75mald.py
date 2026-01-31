# # La Maldición de la Dimensionalidad
# Generar datos aleatorios sintéticos de 3 variables
import numpy as np
# tres vectores numpy random   radint
x = np.random.randint(10, size=10)
y = np.random.randint(10, size=10)
z = np.random.randint(10, size=10)
print(x, y, z)

# Graficar los datos para cada dimensión
import matplotlib.pyplot as plt
#crear gráfica con tres subfiguras
fig = plt.figure(figsize=(18, 6))

#espacio unidimensional
ax = fig.add_subplot(1, 3, 1)    # rejilla de 1 y 3 para ubicar 3 figuras  posicion 1
ax.plot(x, [0]*10, linewidth=0, marker="*",
        color="purple", markersize=20)

#espacio bidimensional
ax = fig.add_subplot(1, 3, 2)
ax.scatter(x, y, marker="*", c="purple", s=200)

#espacio tridimensional
ax = fig.add_subplot(1, 3, 3, projection="3d")
ax.scatter(x, y, z, marker="*", c="purple", s=200)

plt.show()

# el numero de configuraciones aumenta exponencialmente   datos más dispersos
fig = plt.figure(figsize=(18, 6))

# Espacio unidimensional
ax = fig.add_subplot(1, 3, 1)

ax.set_title("10^1 = 10", fontsize=35)   # 10 potenciales nstancias

ax.plot(range(0, 10), [0]*10, 
        marker="o", linewidth=0,
        color="skyblue", markersize=20)

ax.plot(x, [0]*10, linewidth=0,
        marker="*", color="purple",
        markersize=20)


# Espacio bidimensional
ax = fig.add_subplot(1, 3, 2)

ax.set_title("10^2 = 100", fontsize=35)

for i in range(10):
    ax.scatter(range(0, 10), [i]*10,
               s=200, c="skyblue", marker="*")
    
ax.scatter(x, y, marker="*", c="purple", s=200)


# Espacio tridimensional
ax = fig.add_subplot(1, 3, 3, projection="3d")  # 1 3 figuras posicion

ax.set_title("10^3 = 1000", fontsize=35)

for i in range(10):
    for j in range(10):
         ax.scatter(range(0, 10), [i]*10, j, 
                    s=200, c="skyblue", marker="*",
                    alpha=0.25)
ax.scatter(x, y, z, marker="*", c="purple", s=200)

plt.show()

