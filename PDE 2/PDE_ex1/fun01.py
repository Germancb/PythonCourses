# Funciones
def myfun01(manpar, outpar=True):
    if outpar:
        abc=manpar
    else:
        abc="xyz"
    return abc

print(myfun01("german"))
print(myfun01("luis", False))
