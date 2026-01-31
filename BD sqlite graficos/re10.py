import re  #re10.py

lista_nombres=["Ma.1", "S11", "Ma2", "Ba1", "Ma:3", "Va1", "Va3", "Ma4",
               "MaA", "Ma.5", "MaB", "MaC"]

for elemento in lista_nombres:
    if re.findall("Ma[.:]", elemento):
        print(elemento)