import string

with open('persona.txt',"w", encoding="utf-8") as fhand:  # asi no requiere close
    fhand.write("Luis Perez 22\n")
    fhand.write("Maria Marcela Juanes 32\n")

with open("C:/Users/ACER/PYTHON COURSES/DBPY 4/code3/persona.txt","a", encoding="utf-8") as fhand:  # aa append
    fhand.write("Cesar  Montenegro 22\n")
    fhand.write("Luz Emiro Coral 33\n")




