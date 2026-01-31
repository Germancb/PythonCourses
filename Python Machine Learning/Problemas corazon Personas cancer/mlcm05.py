import pandas as pd
from sklearn.model_selection import train_test_split   # separacion datos entrenamiento y prueba 60 20 20

pacientes = pd.read_csv("problemas_del_corazon.csv")   # 100 rows: 50 registros con 1 en cardiaco 50 con 0 (de 1 a 50 y 51 a 100 ordenado)
print(pacientes)

resto, prueba, resto_clase, prueba_clase = train_test_split(
    pacientes[["edad", "genero", "presion", "colesterol", "diabetico"]],
    pacientes["cardiaco"], 
    test_size=0.20)    # Pacientes con columnasa aentrenar 5 -pacietes(cardiaco objetivp y 20% datos para la prueba aleatorios) 80 resto, 
print("prueba")
print(prueba)   # 20 registros
print("resto ")
print(resto)   # 80 rows entrenamieto y validacion indice aleatorio
print("resto_clase ")
print(resto_clase)  # 80
print("prueba_clase")
print(prueba_clase)  #20
entrena, valida, entrena_clase, valida_clase = train_test_split(
    resto[["edad", "genero", "presion", "colesterol", "diabetico"]],
    resto_clase, 
    test_size=0.25)  # 25% dde 80 registros 0 sea 20
print("entrena ")
print(entrena.shape[0])   # 60
print(entrena)   # 60 registros
print(" ")
print("valida size: ", valida.shape[0])  # 20
print(pacientes[pacientes["cardiaco"]==1])   # 0 a 49
