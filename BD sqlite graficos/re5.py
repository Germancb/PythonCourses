import re   # re5.py

lista_nombres=["http://pildorasinformaticas.es",
               "ftp://pildorasinformaticas.es",
               "http://pildorasinformaticas.es.com",
               "ftp://pildorasinformaticas.com"]

for elemento in lista_nombres:
#   if re.findall("es$", elemento):
    if re.findall("^ftp", elemento):
        print(elemento)