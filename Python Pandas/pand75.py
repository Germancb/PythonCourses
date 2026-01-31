import pandas as pd
paises = pd.read_csv("datos_paises.csv", index_col=0)
print(paises)
print(paises[paises["continente"]=="Africa"])

# filtro = paises["km2"]>3287263
print(paises[paises["km2"]>3287263])


print(paises[ (paises["km2"]<50) & (paises["poblacion_miles"]>500)])   # China Macao

print(paises[ (paises["km2"]<5) | (paises["poblacion_miles"]<5) ])

print(paises[(paises["continente"]=="Europa") &
       (paises["km2"]<50) & 
       (paises["poblacion_miles"]<50) ])  #monaco Gibraltar otro


print(paises.loc[~(paises["continente"]=="Europa") &
       (paises["km2"]<50) & 
       (paises["poblacion_miles"]<50) ])    # ojo No europeos