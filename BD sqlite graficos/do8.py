import math    # do8.py usar sqrt devuelve double
def raizCuadrada(listaNumeros):

    """
    La funcion devuelve una lista con la raiz cuadrada con los elementos
    numericos pasados por parametros en otra lista
    ver como se anida con ...
    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4,9,-16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
    ...
    ValueError: math domain error

    """
    return [math.sqrt(n) for n in listaNumeros]

# print(raizCuadrada([9,-16,25,36]))

import doctest
doctest.testmod()
# error por negativo se toma la linea 1 y la última arriba
#Traceback (most recent call last):
#  File "C:\Users\GERMANCB\Python Pildoras\graficos\do7.py", line 16, in <module>
#    print(raizCuadrada([9,-16,25,36]))         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
# otras que da el erro con negativo#
#  ValueError: math domain error     Ultima linea

