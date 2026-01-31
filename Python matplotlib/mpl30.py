import matplotlib.pyplot as plt

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.hist(datos, bins=5, color="pink", ec="black")

plt.show()

import numpy as np

np.random.rand(10)
np.random.normal(loc=5, scale=10, size=1000).std()

datos = np.random.normal(size=1000000)
plt.hist(datos, color="pink", ec="black", alpha=0.5)
plt.title("Distribución Normal")
plt.show()

datos = np.random.uniform(size=1000000)
plt.hist(datos, color="skyblue", ec="black", alpha=0.5)
plt.title("Distribución Uniforme")
plt.show()

datos = np.random.exponential(size=1000000)
plt.hist(datos, color="green", ec="black", alpha=0.5)
plt.title("Distribución Exponencial")
plt.show()