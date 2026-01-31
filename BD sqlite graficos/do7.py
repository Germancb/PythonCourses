import math    # do7.py usar sqrt devuelve double
def raizCuadrada(listaNumeros):
    """
    La funcion devuelve una lista con la raiz cuadrada con los elementos
    numericos pasados por parametros en otra lista
    ver como se anida con ...
    >>> lista=[]
    >>> for i in [4,9,-16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    """
    return [math.sqrt(n) for n in listaNumeros]

print(raizCuadrada([9,-16,25,36]))   #import doctest  # doctest.testmod()

