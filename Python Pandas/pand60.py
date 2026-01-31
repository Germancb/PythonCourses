# manejo diccionarios
import pandas as pd
datos = {"China": [1439, 18.47],
         "India": [1380, 17.70],
         "Estados Unidos": [331, 4.25],
         "Indonesia": [273, 3.51], 
         "Pakistán": [220, 2.83],
         "Brasil": [212, 2.73], 
         "Nigeria": [206, 2.64],
         "Bangladesh": [164, 2.11],
         "Rusia": [145, 1.87],
         "México": [128, 1.65]}

encabezado = ["poblacion", "porcentaje"]

paises = pd.DataFrame(datos, index=encabezado)
paises = paises.T
paises
print(paises)
print(paises.dtypes)
print(paises.index)
print(paises.values)
# paises.index, paises.columns
print(paises.iloc[0], paises.loc["China"])   # loc 0
print(paises.sort_index())

tasa_fertilidad = [1.7, 2.2, 1.8, 2.3, 3.6, 1.7, 5.4, 2.1, 1.8, 2.1]
paises["tasa_fertilidad"] = tasa_fertilidad
print(paises)

paises.pop("tasa_fertilidad") 
#del paises["tasa_fertilidad"]
#paises.drop("tasa_fertilidad", axis=1, inplace=True)

# Japón -> 126, 1.62 
renglon = pd.Series(name="Japón", data=[126, 1.62], index=["poblacion", "porcentaje"])
renglon
paises = paises._append(renglon)   # ojo ._append    no .append
print(paises)

# paises.drop(["Japón"], axis=0, inplace=True)
# paises.describe(), paises.min()

paises.boxplot()
