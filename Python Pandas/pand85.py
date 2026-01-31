import pandas as pd

datos = pd.read_csv("datos/clientes.csv")

print(datos["nombre"])
print(datos[ datos["nombre"].isnull() ])
# print(datos.dropna(subset=["nombre", "ingreso"], inplace=True))
# print(datos.dropna())
print(datos)
print(datos.fillna(0))
print(datos["nombre"].fillna("DESCONOCIDO"))

promedio = datos["ingreso"].mean()
mediana = datos["ingreso"].median()
moda = datos["ingreso"].mode()[0]
print(promedio, mediana, moda)
print(datos["ingreso"].fillna(moda))