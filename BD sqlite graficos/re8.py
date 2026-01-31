import re #re8.py

lista_nombres=["Ana", "Pedro", "Maria", "Rosa", "Sandra", "Celia", "Orlando"]

for elemento in lista_nombres:
#   if re.findall("[o-t]", elemento): 
    if re.findall("^[O-T]", elemento):
        print(elemento)