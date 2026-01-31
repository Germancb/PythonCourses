import re  #re11.py
nombre1="Sandra Lopez"
nombre2="Antonio Gomez"
nombre3="sandra Lopez"

if re.match("Sandra", nombre3, re.IGNORECASE):
    print("encontramos el nombre")
else:
    print("No se encontro")
