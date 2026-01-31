import re  # re7.oy

lista_nombres=["hombres", "mujeres", "mascotas", "niños", "niñas"]

for elemento in lista_nombres:
#   if re.findall("es$", elemento):
#    if re.findall("[ñ]", elemento):
#   if re.findall("cami[oó]n")
    if re.findall("niñ[oa]s", elemento):
        print(elemento)