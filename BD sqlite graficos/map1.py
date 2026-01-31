class Empleado:
    def __init__(self, nombre,cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} U$".format(self.nombre, self.cargo, self.salario)

listaEmpleados=[
               
     Empleado("Juan", "Director", 7500),   
     Empleado("Luis", "Presidente", 10000),  
     Empleado("Ana", "Administrativo", 2500),  
     Empleado("Juana", "Secretaria", 2700),      
     Empleado("Jack", "Botones", 2100),                     
]

def calculo_comision(empleado):
    if(empleado.salario<=3000):
        empleado.salario=empleado.salario*1.03
    return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)