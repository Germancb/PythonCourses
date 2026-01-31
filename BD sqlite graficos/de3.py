# de3.py  *args
def funcion_decoradora(funcion_parametro): ## A yB
    def funcion_interior(*args, **kwargs): # C  #Acciones adicinales antes y despues
        print("Vamos a realizar un calculo")
        funcion_parametro(*args,**kwargs)
        print("Terminado el calculo")
    return funcion_interior   # Corresponde a decoradora

@funcion_decoradora  #vamos a decorar la funcion suma (funcion parámetro)
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))   #claves

suma(17, 5, 45)
resta(25,10)
potencia(base=5,exponente=3)   # argumentos con clave kwargs base y exponente