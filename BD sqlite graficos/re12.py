import re  #re12.py
nombre1="Jara Lopez"
nombre2="Antonio Gomez"
nombre3="Lara Lopez"

if re.match(".ara", nombre3, re.IGNORECASE):
    print("encontramos el nombre")
else:
    print("No se encontro")
