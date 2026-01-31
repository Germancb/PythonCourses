# de1.py funcion decoradora sintaxis Antes/despues de realizar la funcion suma/resta un msg  
def funcion_decoradora(funcion_parametro): ## A yB
    def funcion_interior(): # C    #   Acciones adicinales antes y despues
        print("Vamos a realizar un calculo")
        funcion_parametro()
        print("Terminado el calculo")
    return funcion_interior   # Corresponde a decoradora

@funcion_decoradora  #vamos a decorar la funcion suma (funcion parámetro)
def suma():
    print(15+10)
@funcion_decoradora
def resta():
    print(15-10)

suma()
resta()