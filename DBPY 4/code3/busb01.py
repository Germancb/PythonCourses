# busqueda binaria
lista = [11,12,13,14,15,16,17, 9, 10]
lista.sort()
valb = 0
valido = 1
try:
    valb = int(input("entre un numero entre 9 y 17: "))
    if valb < 9 or valb > 17:
        print("numero invalido")
        valido = 0
except:
    print("Valor invalido")
    valido = 0
    exit
#for i in lista:
#    if i == valb:
#        print("si")
while valido == 1:
    if valb in lista:
        print("si ", valb)  

    print(lista)
    bajo = lista[0]
    print(bajo)
    print(len(lista))
    alto=lista[len(lista)-1]
    print(alto)
    medio=(alto+bajo)//2
    pcentro=(len(lista)-1)//2
    for i in lista:
        if i == valb:
            print(i)
    print(pcentro)
    if valb > medio:
        print("alto")
    elif valb == medio:
        print("Centro")
    else:
        print("bajo")
    valido = 0