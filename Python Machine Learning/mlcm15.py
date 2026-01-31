import numpy as np
import matplotlib.pyplot as plt
import math
logistica = np.frompyfunc(lambda b0, b1, x:
                         1 / (1 + math.exp(-(b0 + b1*x))),
                         3, 1)   # funcion numpy muy eficiente   3 = numero parametros funcion lambda (b0,b1 y x) y 1 un parametro salida

# taqucardia probabilidad y clase  # EJEMPLO DE USO PARA CLASIFICAR EN DOS CLASES NORMAL y con  taquicardia
# Persona Normal de 60 a 100 latidos por minuto.
# Persona con Taquicardia de hasta 220 latidos por minuto.
personas_normal = [65, 70, 80, 80, 80,
                   90, 95, 100, 105, 110]

personas_taquicardia = [105, 110, 110, 120, 120,
                        130, 140, 180, 185, 190]
# Persona Normal de 60 a 100 latidos por minuto.
# Persona con Taquicardia de hasta 220 latidos por minuto.

# Graficamos una función logística con diferemtes pendientes
plt.figure(figsize=(6, 4))   # Pendientes
plt.scatter(np.arange(-5, 5, 0.1), 
            logistica(0, 1,np.arange(-5, 5, 0.1)),
            color = "green")    # Pendiente 1 se cambia o prueba con 2 y 3  0, 1, np.arange(...)  La mejor en este caso 3
plt.show()
