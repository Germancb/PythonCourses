class Empleado:
    def __init__(self, nombre,cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} U$".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
               
     Empleado("Juan", "Director", 75000),   
     Empleado("Luis", "Presidente", 100000),  
     Empleado("Ana", "Administrativo", 25000),  
     Empleado("Juana", "Secretaria", 27000),      
     Empleado("Jack", "Botones", 21000),                     
]

salarios_altos=filter(lambda empleado:empleado.salario>50000,listaEmpleados)

for empleado_s in salarios_altos:
    print(empleado_s)