#  Clusters con DBSCAN y Scikit-learn  DENSITY-BASED Spatial Clustering of applications with noise
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Cargar datos
datos = np.loadtxt("casas.csv", delimiter=",")

# Identificar Clusters
clusters = DBSCAN(eps=2, min_samples=10).fit_predict(datos)   # MIn_sample = 10 minimo numero de puntos para determinar si un area es densa o no esp= 2 por experimentación
print(clusters)   # -1 ruido 0, 1,2   etiqueta clusters

# Gráfica de matplotlib para mostrar los Clusters
plt.figure(figsize=(7.5, 7.5))
plt.scatter(datos[:, 0], datos[:, 1], c=clusters, s=100)
print("ver  : "      )
#print(datos[:, 0])
# print(datos[:, 1])
plt.xlabel("Antigüedad de la Construcción en Años")
plt.ylabel("Precio de Casa en Pesos (1:100,000)")
plt.box(False)
plt.show()