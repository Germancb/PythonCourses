
def compruebaMail(mailUsuario):   # do5.py
    """La funcion compruebaMail evalua mail en busca de una (1) @
    si recibe mas de una está mal y no puede ir al final
    
    """
    arroba=mailUsuario.count('@')
    if(arroba!=1 or mailUsuario.rfind('@')==len(mailUsuario-1) or 
       mailUsuario.find('@')==0):
        return False
    else: 
        return True

import doctest
doctest.testmod()

# help(Areas.areatriangulo)
# print(areatriangulo(4, 8))