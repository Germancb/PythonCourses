
import numpy as np
# Anaisis de datos Por row per columns

altura_y_pesos = np.array([[ 1.74, 91.40 ],
                           [ 1.80, 88.70 ],
                           [ 1.78, 87.30 ],
                           [ 1.68, 62.70 ],
                           [ 1.78, 81.60 ]])

print("Minimo", altura_y_pesos.min())
print("Maximo", altura_y_pesos.max())
print("Pos Min", altura_y_pesos.argmin())  # posicio del mim
print("Pos Max", altura_y_pesos.argmax())
print("Suma", altura_y_pesos.sum())
print("Promedio", altura_y_pesos.mean())

print("ndim ", altura_y_pesos.ndim)
print("shape ", altura_y_pesos.shape)

max=0
i=0
while i < 4:
    print(altura_y_pesos[i][0])
    i = i  + 1
    if altura_y_pesos[i][0] > max:
        max = altura_y_pesos[i][0]
print("maximo ", max)

print("Minimo", altura_y_pesos.min(axis=0))    
print("Maximo", altura_y_pesos.max(axis=0))
print("Pos Min", altura_y_pesos.argmin(axis=0))
print("Pos Max", altura_y_pesos.argmax(axis=0))
print("Suma", altura_y_pesos.sum(axis=0))
print("Promedio", altura_y_pesos.mean(axis=0))
print(" ")
print("Minimo", altura_y_pesos.min(axis=1))    
print("Maximo", altura_y_pesos.max(axis=1))
print("Pos Min", altura_y_pesos.argmin(axis=1))
print("Pos Max", altura_y_pesos.argmax(axis=1))
print("Suma", altura_y_pesos.sum(axis=1))
print("Promedio", altura_y_pesos.mean(axis=1))
print(" ")
print(altura_y_pesos.transpose())

