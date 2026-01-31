from random import randint

class Tragamonedas:

    def __init__(self, id, premio):
        self.id = id
        self.premio = premio
        self.monedas = 0
        self.jackpot = 0
        print('This is Tragamonedas')
    def __str__(self):
        return "Id: " + str(self.id) + " Premio: " + str(self.premio)

    def jugar(self):
    #    pass
        self.monedas +=1
        numeros = randint(0, 9), randint(0,9), randint(0, 9)
        mensaje=""
        if numeros[0] == numeros[1] == numeros[2]:
            self.jackpot +=1
            mensaje = "Felicidades!!! Ganaste %0.2f" % self.premio
        else:
            mensaje = "Suerte en la proxima!!!"
            # print(mensaje)
            # print("Suerte en la proxima")
        return numeros, mensaje
    
tragamonedas_a = Tragamonedas(1,1000)
tragamonedas_b = Tragamonedas(2, 700)

# print(tragamonedas_a.jugar())
# print(tragamonedas_b.jugar())

for i in range(100):
    print(tragamonedas_a.jugar())
    print(tragamonedas_b.jugar())

print(tragamonedas_a.jackpot)
print(tragamonedas_b.jackpot)

print(tragamonedas_a)
print(tragamonedas_b)