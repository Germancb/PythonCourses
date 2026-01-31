class Vehiculos():   #Clase padre    modu_vehi.py
#   Estado inicial Propiedades
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
# definir Funciones y estado (puede arrancar)
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ",self.marca,"\nModelo ",self.modelo,"\nEn marcha: ",self.enmarcha,"\n",
       "Acelera: ", self.acelera,"\n", "Frenar: ", self.frena,"\n")

class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado=cargar    # se iguala a cargar
        if(self.cargado):   # True
            return "La furgoneta esta cargada "
        else:
            return "Furgoneta sin carga"

class Moto(Vehiculos):
    def caballito(self):
        self.hcaballito="Estoy haciendo el caballito"

    def estado(self):
        print("Marca: ",self.marca,"\nModelo ",self.modelo,"\nEn marcha: ",self.enmarcha,"\n",
       "Acelera: ", self.acelera,"\n", "Frenar: ", self.frena,"\n", self.hcaballito)
# pass
class VElectricos(Vehiculos):  #adicio Vehiculospor uso super
    def __init__(self,marca, modelo):  #adicion marca y modelo con suér()..

        super().__init__(marca, modelo)

        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

class BicicletaElectrica(VElectricos, Vehiculos):
    pass

