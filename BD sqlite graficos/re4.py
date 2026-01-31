import re   # re4.py

lista_nombres=["Ana Gomez", "Sandra Alvarez", "Maria Martin", "Sandra Lopez",
               "Santiago Martin"]

for elemento in lista_nombres:
#   if re.findall("^Sandra", elemento):
    if re.findall("Martin$", elemento):
        print(elemento)