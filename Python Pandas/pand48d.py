import pandas as pd

ventas = pd.read_excel("datos/ventas_anuales.xlsx", index_col=0,
                    skiprows=1, sheet_name=None)    # le e2020 y 2021 solo 2021 ->"2021")
print(ventas)
print(ventas["2021"])



