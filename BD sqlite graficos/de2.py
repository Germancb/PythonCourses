#  de2.py  *args    
def funcion_decoradora(funcion_parametro): ## A yB
    def funcion_interior(*args): # C   #  Acciones adicinales antes y despues
        print("Vamos a realizar un calculo")
        funcion_parametro(*args)
        print("Terminado el calculo")
    return funcion_interior   # Corresponde a decoradora

@funcion_decoradora  #vamos a decorar la funcion suma (funcion parámetro)
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

def potencia(base, exponente):
    print(pow(base, exponente))
suma(17, 5, 45)
resta(25,10)
potencia(10,6)