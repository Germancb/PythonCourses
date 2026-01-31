# prueba while true
max = 0
min = 0
while True:
    inum= input("Entre un numero o fin: ")
    if inum =="fin":
        print(" fin del programa")
        print("maximo: ",max, "minimo: ", min)
        exit()
    try:
        inum=float(inum)
    except:
        print("no es un número ")
        continue
    if inum < min:
        min = inum
    if inum > max:
        max = inum
