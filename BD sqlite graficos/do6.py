def compruebaMail(mailUsuario):   # do6.py
    """La funcion compruebaMail evalua mail en busca de una (1) @
    si recibe mas de una está mal y no puede ir al final

    >>> compruebaMail('juan@curso.es')
    True

    >>> compruebaMail('jancurso.es')
    False

    >>> compruebaMail('juancurso.es@')
    False

    >>> compruebaMail('juan@curso.es@')
    False
    """
    arroba=mailUsuario.count('@')
    if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1)
        or mailUsuario.find('@')==0):
        return False
    else: 
        return True


import doctest
doctest.testmod()

# help(Areas.areatriangulo)
# print(areatriangulo(4, 8))
"""">>> compruebaMail('juancurso.es')
    False
    >>> compruebaMail('juancurso.es@')
    False
    >>> compruebaMail('juan@curso.es@')
    False  """  