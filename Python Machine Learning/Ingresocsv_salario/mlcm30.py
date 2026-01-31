# %% ARBOLES
import pandas as pd 
from random import sample

personas = pd.read_csv("ingresos.csv")   # ingreso alto=1, no=0
# %% muestreo con reemplazo
print(personas.sample(frac=2/3, replace=True))   # metodo samp'le  bootsrap
print(personas.sample(frac=2/3, replace=True))
print(personas.sample(frac=2/3, replace=True))
print(personas.sample(frac=2/3, replace=True))
print(personas.sample(frac=2/3, replace=True))

print(personas.columns[:-1], "\n")   #todas las columnas menos ingreso (:-1) Columnas: edad estudio genero tipo_tabajo  horas ingreso
# print(sample(set(personas.columns[:-1]), 3))  # Seleccina tres de las 5 caracteristicas (columnas menos ingreso)
# %% Construccion del bosque Ramdon Forest
from sklearn.ensemble import RandomForestClassifier

bosque = RandomForestClassifier(n_estimators=100,
                               criterion="gini",
                               max_features="sqrt",
                               bootstrap=True,
                               max_samples=2/3,
                               oob_score=True)   # 100 arboles diferentes Default=100. Uso el Gini (Otro:entropia), caracteristicas a tomar:raiz_cuadrada del numero de caracteristicas
                                                # bootstrap muestreo aleatorio, Porcentaje a muestrear 2/3, oob:score activado, métrica especial para bosques c/100 usa 2/3 el 1/3 que no queda seisa para evauar
# %% Crear bosue, con que carateristicas (todas - 1:ingreso, la clase es ingreso  Objetos de arreglos numpy vom .values
bosque.fit(personas[personas.columns[:-1]].values, personas["ingreso"].values)  # 

print(bosque.predict([[50, 16, 1, 1, 40]]))   # ejecutar prediccion con lista de listas: 50 años 16 de estudio genero=1 trabaja sectro privado semanalmente 40 horas en promedio
print(bosque.score(personas[personas.columns[:-1]].values, personas["ingreso"].values))   # score con los mismos datos de creacion   # 0.97
print(bosque.oob_score_)   # 0.75 0.76

import matplotlib.pyplot as plt
from sklearn import tree

for arbol in bosque.estimators_:
    tree.plot_tree(arbol, feature_names=personas.columns[:-1])
    plt.show()  # 100 graficas OJO