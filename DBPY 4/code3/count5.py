
pasajeros = {}

with open("estaciones.csv", "r", encoding="utf-8") as archivo:
    archivo.readline()  # Elimina ebcabezado
    estaciones = archivo.readlines()  # info relevante
    for estacion in estaciones:
        lista = estacion.strip().split(",") 
        pasajeros[lista[0]] = list(map(int,lista[1:]))      # map convierte a enteros
print(pasajeros)


