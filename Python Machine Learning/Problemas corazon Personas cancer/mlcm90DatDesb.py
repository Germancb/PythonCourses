# Cómo crear Clasificadores de Machine Learning ante Clases Desbalanceadas asignando Pesos con Python
# Datos desbalanceados Sub y sobre muestreo
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score 

# Código de soporte 

def matriz_de_confusion(clases_reales, clases_predichas, titulo):
    """ Visualiza la matriz de confusión """
    print("Reales:", clases_reales.reshape(-1))
    print("Predichas:", clases_predichas)
    matriz = confusion_matrix(clases_reales, clases_predichas)
    accuracy = accuracy_score(clases_reales, clases_predichas)
    
    #Código de matplotlib para graficar 
    plt.figure(figsize=(4, 4))
    matriz = pd.DataFrame(matriz, 
                          columns=["0 : Sana", "1 : Cáncer"])
    plt.matshow(matriz, cmap="Pastel1", vmin=0, vmax=20, fignum=1)
    plt.xticks(range(len(matriz.columns)), matriz.columns, rotation=45)
    plt.yticks(range(len(matriz.columns)), matriz.columns)
    etiquetas = (("Verdaderos\nnegativos", "Falsos\npositivos"),
                 ("Falsos\nnegativos", "Verdaderos\npositivos"))
    plt.text(1.60, -0.30, titulo, fontsize=25, c="red")
    plt.text(2.1, 0.10, "Accuracy: %0.2f" % accuracy, fontsize=20)
    for i in range(len(matriz.columns)):
        for j in range(len(matriz.columns)):
            plt.text(i, j + 0.14, str(matriz.iloc[i, j]),
                     fontsize=30, ha="center", va="center")
            plt.text(i, j - 0.25, etiquetas[i][j],
                     fontsize=11.5, ha="center", va="center")           
    plt.show()

# University of Wisconsin, Clinical Sciences Center 
# 30 características: radio, textura, area, entre otros
# 0 : SANAS, 1 : CÁNCER
personas = pd.read_csv("cancer_desbalance.csv", header=None)
prueba = pd.read_csv("cancer_prueba.csv", header=None)

# Gráficas de barras
num_sanas = personas[personas[30]==0][0].size
num_cancer = personas[personas[30]==1][0].size
plt.bar(["Sanas (%d)" % num_sanas, "Cáncer (%d)" % num_cancer], 
        [num_sanas, num_cancer],
        color =["cyan", "red"],
        width = 0.8)
plt.ylabel("Personas")
plt.show()

#Separando los datos por Clase
datos_cancer = personas[personas[30]==1]
datos_sanas = personas[personas[30]==0]
# Sobremuestreo con Remplazo
sobremuestreo_cancer = datos_cancer.sample(n=290, replace=True, random_state=0)
sobremuestreo_cancer
# Submuestreo sin Remplazo
submuestreo_sanas = datos_sanas.sample(n=20, replace=False, random_state=0)
submuestreo_sanas
# Preparando los datos para tres clasificadores
sobremuestro = pd.concat([sobremuestreo_cancer, datos_sanas])
datos_sobremuestreo = sobremuestro.iloc[:, :-1]
clase_sobremuestreo = sobremuestro.iloc[:, -1:]

submuestreo = pd.concat([datos_cancer, submuestreo_sanas])
datos_submuestreo = submuestreo.iloc[:, :-1]
clase_submuestreo = submuestreo.iloc[:, -1:]

desbalanceado = pd.concat([datos_cancer, datos_sanas])
datos_desbalanceado = desbalanceado.iloc[:, :-1]
clase_desbalanceado = desbalanceado.iloc[:, -1:]

# Datos para probar los modelos (son solo 20 instancias)
datos_prueba = prueba.iloc[:, :-1]
clase_prueba = prueba.iloc[:, -1:]
#Creación y Evaluación de 3 Modelos
# Regresión Logística
modelo = LogisticRegression().fit(datos_desbalanceado.values, 
                                  clase_desbalanceado.values.reshape(-1))
matriz_de_confusion(clase_prueba.values, 
                    modelo.predict(datos_prueba.values), 
                    "Desbalanceado") 

modelo = LogisticRegression().fit(datos_submuestreo.values, 
                                  clase_submuestreo.values.reshape(-1))
matriz_de_confusion(clase_prueba.values, 
                    modelo.predict(datos_prueba.values), 
                    "Submuestreo") 

modelo = LogisticRegression().fit(datos_sobremuestreo.values, 
                                  clase_sobremuestreo.values.reshape(-1))
matriz_de_confusion(clase_prueba.values, 
                    modelo.predict(datos_prueba.values), 
                    "Sobremuestreo") 
# Reales: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Predichas: [0. 1. 0. 1. 1. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]