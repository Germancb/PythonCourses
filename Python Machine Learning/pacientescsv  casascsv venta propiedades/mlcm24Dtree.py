import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import entropy
from math import log
# Entropia Promedio de informacion almacenada en una variable aleatoria
pacientes = pd.read_csv("pacientes.csv")

edades = pd.Series([40, 30, 20, 50])
colesterol = pd.Series([100, 110, 100, 110])

print(edades.value_counts()/edades.size)
print(colesterol.value_counts()/colesterol.size)
print(entropy(edades.value_counts()/edades.size, base=2))
print(entropy(colesterol.value_counts()/colesterol.size, base=2))

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

datos_entrena, datos_prueba, clase_entrena, clase_prueba = train_test_split(
    pacientes[["edad", "colesterol"]],
    pacientes["problema_cardiaco"], 
    test_size=0.30)


arbol_decision = tree.DecisionTreeClassifier(criterion="entropy")
# arbol_decision = tree.DecisionTreeClassifier(criterion="entropy", max_depth=2)

arbol = arbol_decision.fit(datos_entrena, clase_entrena)

accuracy = arbol_decision.score(datos_prueba, clase_prueba)  # tantas vecers clasifico correctamente

print(accuracy)

print(tree.export_text(arbol,
                      feature_names=["Edad", "Colesterol"]))   # Exportar a texto
plt.figure(figsize=(12, 6))   #tamaño figur
tree.plot_tree(arbol, 
              feature_names=["Edad", "Colesterol"])
plt.show()

print("Nuevo paciente", arbol_decision.predict([[70, 150]]))


