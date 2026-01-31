import re  #re6.py

lista_nombres=["http://informaticaenespaña.es",
               "http://pildorasinformaticas.es",
               "http://pildorasinformaticas.com"]

for elemento in lista_nombres:
#   if re.findall("es$", elemento):
    if re.findall("[ñ]", elemento):
        print(elemento)