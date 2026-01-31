import re   #re13.py
cadena1="Jara Lopez"
cadena2="596541"
cadena3="a45789"

if re.match("\d", cadena2, re.IGNORECASE):
    print("encontramos el número")
else:
    print("No se encontro")
