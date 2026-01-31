from Modupy import fun_mat    #do3.py
class Areas:
    """Esta calse calcula areas cuadrado y triangulo"""
    def areaCuadrado(lado):
        """ Calcula el area de un cuadrado elevando el lado -parametro al cuadraro"""
        return "El area del cuadrado es: " + str(lado*lado)

    def areatriangulo(base, altura):        
        """Calcula area triangulo mult base por altura y la div por 2"""
        return "El area del triangulo es: " + str((base*altura)/2)

help(fun_mat)
help(Areas)  #ayuda general
print(Areas.areaCuadrado(5))
print(Areas.areaCuadrado.__doc__)
help(Areas.areatriangulo)
print(Areas.areatriangulo(4, 8))