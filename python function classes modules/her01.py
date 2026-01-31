# Herencia Clase Padre Producto
# Hijas: Perecederos y Electronica Polimorfismo

class Producto:

    def __init__(self, id, descripcion, costo):
        self.id = id
        self.descripcion = descripcion
        self.costo = costo

    def crear_etiqueta(self):
        return " %s \n %s \n %0.2f \n" % (self.id,
                                        self.descripcion,
                                        self.costo)
    #sobrecarga de métodos con crear_etiqueta

class Perecedero(Producto):

    def __init__(self, id, descripcion, costo, fecha_cad):
        super().__init__(id, descripcion, costo)
        self.fecha_cad = fecha_cad

    def crear_etiqueta(self):
        return super().crear_etiqueta() + " %s \n" % self.fecha_cad
        
class Electronico(Producto):

    def __init__(self, id, descripcion, costo, marca):
        super().__init__(id, descripcion, costo)
        self.marca = marca

    def crear_etiqueta(self):
        return super().crear_etiqueta() + " %s \n" % self.marca

pro = Producto("g", "Generico", 100)
per = Perecedero("p", "Jitomate", 200, "01/01/2020")
ele = Electronico("e", "Lavadora", 300, "Sony")
# POLIMORFISMO
objetos = (pro, per, ele)
# objeto adopta multiples formas
for objeto in objetos:
    print(objeto.crear_etiqueta(), type(objeto))

print(isinstance(pro, Producto))   # True
print(isinstance(pro, Electronico))   #False

#print(pro.crear_etiqueta())
#print(per.crear_etiqueta())
# print(ele.crear_etiqueta())