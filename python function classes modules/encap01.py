# EMCAPSULAMIENTO   Proteger ejm balance
# Atributos publicos y privados
class Cuenta:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.__balance = 0.00    # __balance atributo privado ojo
        
    # def __str__(self):
    #   return str(self.serie) + " " + self.color
    # def __retirar    con los __retirar lo vuelvo privado
    def retirar(self, monto):
        if self.__balance >= monto:
            self.__balance  -= monto
        else:
            print("balance insuficinte")

    def depositar(self, monto):
        if monto > 0:
            self.__balance  += monto
        else:
            print("Deposito negativo. Error")
    
cuenta = Cuenta("Juan Perez", "Reforma 100")
cuenta.depositar(1000)

cuenta.retirar(2000)

print(cuenta._Cuenta__balance)
print(cuenta.nombre)