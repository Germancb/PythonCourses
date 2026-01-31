numint = 0
while True:
    b = input("Entre un número o fin para terminar: ")
    if b == ("fin"):
        print("dio fin  ")
        break
    try:
        b1 = float(b)
    except:
        print("El Valor no es válido ")
        numint = numint + 1
        if numint  == 4:
            print("mas de 3 intentos ")
            break
print("Dió un ", b)
    
    
