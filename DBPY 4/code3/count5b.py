
pasajeros = {}

with open("estaciones.csv", "r", encoding="utf-8") as archivo:
    archivo.readline()  # Elimina ebcabezado
    estaciones = archivo.readlines()  # info relevante
    for estacion in estaciones:
        lista = estacion.strip().split(",") 
        listv = []
        for i in lista:
            listv.append(i)
        pasajeros[lista[0]] = listv     
print(pasajeros)


