import pandas as pd

datos = {"pais" : ["Estados Unidos", "China", "Brasil", "India", "México"],
         "km2": [9833517, 9600000, 8515767, 3287263, 1964375]}

paises = pd.DataFrame(datos)
print(paises)

filtro = [True, False, False, False, True]
print(paises[filtro])

print(paises[paises["km2"]>3287263])