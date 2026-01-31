# modelo  de REGRESION LOGISTICA  Calculo b0 y b1
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

frecuencias_cardiacas = [[65], [70], [80], [80], [80],
                         [90], [95], [100], [105], [110],
                         [105], [110], [110], [120], [120],
                         [130], [140], [180], [185], [190]]   #lista de listas con 1 variable

clase = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Creamos conjuntos de entrenamiento y de prueba del modelo
datos_entrena, datos_prueba, clase_entrena, clase_prueba = \
    train_test_split(frecuencias_cardiacas,
                     clase, 
                     test_size=0.30)  # 30% de los datos para probar

# Creamos el modelo de Regresión Logística

modelo = LogisticRegression().fit(datos_entrena, clase_entrena)   # Metodo fit usados port sklearn
np.set_printoptions(suppress=True)   
print(modelo.predict(datos_prueba))   # # [0 0 1 0 1 0]   # cambia con cada corrida porque se seleccionan datos aleatoriamente
print("datos_prueba ")
print(modelo.predict_proba(datos_prueba))   # probabilidades  no pertenecer si a la clase taquicardia
print(modelo.score(datos_prueba, clase_prueba)) # 0.8333333333333334  0.666666  score o accuracy
print(modelo.intercept_, modelo.coef_)  # Ojo b0 y b1   [-59.27351516] [[0.54381627]]