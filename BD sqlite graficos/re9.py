import re  #re9.py

lista_nombres=["Ma1", "S11", "Ma2", "Ba1", "Ma3", "Va1",
               "Va3", "Ma4", "MaA", "Ma5", "MaB", "MaC"]

for elemento in lista_nombres:
#   if re.findall("[o-t]", elemento): 
#   if re.findall("Ma[0-3]", elemento):
#    if re.findall("Ma[^0-3]", elemento):  #Rango negado
    if re.findall("Ma[0-3A-B]", elemento):
        print(elemento)