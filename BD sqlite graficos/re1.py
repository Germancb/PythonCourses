import re   # re1.py
cadena="Vamos a aprender expresiones regulares"
print(re.search("aprender", cadena))
textBuscar=("aprender")

if re.search(textBuscar, cadena)!="None":
    print("se ha encontrado e1 texto")
else:
    print("No se ha encontrado el texto")

