def areatriangulo(base, altura):        #do4.py
    """Calcula area triangulo mult base por altura 
    >>> areatriangulo(3,6)  
    'El area del triangulo es: 9.0'

    >>> areatriangulo(4,5)  
    'El area del triangulo es: 10.0'

    >>> areatriangulo(9,3)  
    'El area del triangulo es: 13.5'
    
    """
    return "El area del triangulo es: " + str((base*altura)/2)
#   return (base*altura/2)
import doctest
doctest.testmod()

# help(Areas.areatriangulo)
# print(areatriangulo(4, 8))