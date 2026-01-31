import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

datos = pd.read_csv("ingreso.csv")
print(datos)

plt.ylabel("Ingreso ($)")
plt.xlabel("Promedio de horas semanales trabajadas")
plt.scatter(datos["horas"], datos["ingreso"], color="pink")
plt.show()

regresion = linear_model.LinearRegression()
# print(datos["horas"].values)  # un vector numpy
horas = datos["horas"].values.reshape((-1, 1))  # vector con multiples vectores

modelo = regresion.fit(horas, datos["ingreso"])

print("Intersección (b)", modelo.intercept_)
print("Pendiente (m)", modelo.coef_)

entrada = [[39.5], [40], [43], [43.5]]
print(modelo.predict(entrada))

plt.scatter(entrada, modelo.predict(entrada), color="red")
plt.plot(entrada, modelo.predict(entrada), color="black")

plt.ylabel("Ingreso ($)")
plt.xlabel("Promedio de horas semanales trabajadas")
plt.scatter(datos["horas"], datos["ingreso"], color="pink", alpha=0.55)
plt.show()

