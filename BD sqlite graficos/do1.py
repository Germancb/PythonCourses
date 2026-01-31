def areaCuadrado(lado):   #do1.py
    """ Calcula el area de un cuadrado elevando el lado -parametro al cuadraro"""
    return "El area del cuadrado es: " + str(lado*lado)

def areatriangulo(base, altura):
    """Calcula area triangulo mult base por altura y la div por 2"""
    return "El area del triangulo es: " + str((base*altura)/2)

print(areaCuadrado(5))
print(areaCuadrado.__doc__)
help(areatriangulo)
print(areatriangulo(4, 8))