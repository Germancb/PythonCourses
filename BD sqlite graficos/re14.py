import re   # re14.py
nombre1="Jara Lopez"
nombre2="Antonio Gomez"
nombre3="Lara Lopez"

if re.search("Lopez", nombre3, re.IGNORECASE):
    print("encontramos el nombre")
else:
    print("No se encontro")
