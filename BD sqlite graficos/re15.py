import re   #re15.py
codigo1="Jara Lopez 71 bbbbbbre"
codigo2="ad71 Antonio Gomez"
codigo3="edrty Lara Lopez"

if re.search("71", codigo1):
    print("encontramos el 71")
else:
    print("No se encontro")
