import pandas as pd   # lists de listas cada col serie

nombre_paises = ["China", "India", "Estados Unidos", "Indonesia", "Pakistán",
                 "Brasil", "Nigeria", "Bangladesh", "Rusia", "México"]

encabezado = ["poblacion", "porcentaje"]

datos = [[1439, 18.47],
        [1380, 17.70],
        [331, 4.25],
        [273, 3.51], 
        [220, 2.83],
        [212, 2.73], 
        [206, 2.64],
        [164, 2.11],
        [145, 1.87],
        [128, 1.65]]

paises = pd.DataFrame(datos, index=nombre_paises, columns=encabezado)
print(paises)
print(paises.dtypes)
print(paises.index)
print(paises.values)