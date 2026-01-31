def escribir(nombre, texto):
    with open(nombre, "w") as archivo:
        archivo.write(texto)

def leer(nombre):
    texto=""
    with open(nombre, "r") as archivo:
         texto= archivo.read()
    return texto

escribir("prueba.txt", "Un texto cualquiera")
print(leer("prueba.txt"))
