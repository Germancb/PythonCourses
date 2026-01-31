def crea_clave(nombre, anon):
    clave=""
    for ln in nombre.split():
        clave=clave + ln[0].upper()
        
    anon = str(anon)
    clave=clave+anon[-2:]
    return clave

print(crea_clave("German cordoba Barahona", 1949))

