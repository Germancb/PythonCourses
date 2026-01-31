#Atributos de Clase

class Vehiculo:
    folio = 0
    COLORES = ("BLANCO", "ROJO", "VERDE") # Colores validos
    # Atributos de clase: Vehiculo.folio  serie se incrementa en 1
    # def __init__(self, serie, color):
    def __init__(self, color):
        Vehiculo.folio +=1   # atributo de clase compartido entre todos
        self.serie = Vehiculo.folio
        self.set_color(color)
        #self.color=color
        
    def __str__(self):
        return str(self.serie) + " " + self.color
    # Metodo validador de colores setter
    def set_color(self, color):
        color = color.upper().strip()    # mayusculas y sin blancos al inicio final
        if color in Vehiculo.COLORES:
            self.color = color.upper()
        else:
            self.color = Vehiculo.COLORES[0]   # asigno color Blanco por default
    
    #sobrecarga de métodos con crear_etiqueta

#vehiculo_a= Vehiculo(1, "ROJO")
# vehiculo_b = Vehiculo(2, "VERDE")
vehiculo_a= Vehiculo("Rojo")
vehiculo_b = Vehiculo("VERDE")

print(vehiculo_a)
print(vehiculo_b)

print(vehiculo_a.serie)
print(vehiculo_b.folio)
