# discretizar datos numericos
import numpy as np
import pandas as pd

edades = np.array([1, 7, 8, 15, 16, 28, 35, 50, 55, 70, 75, 100])

resultado = pd.cut(edades,
                   bins = [0, 11, 17, 59, np.inf],
                   labels = ["infante", "joven","adulto", "mayor"],
                   include_lowest=True,
                   retbins=True)
print(resultado[1], "\n")
print(resultado[0].codes, "\n")
print(resultado[0].categories, "\n")
print(np.array(resultado[0]), "\n")
