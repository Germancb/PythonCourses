import string
fhand = open('romeo.txt', encoding="utf-8")
texto= fhand.read()
print(texto)
nl = 0
fhand.close()
fhand = open('romeo.txt', encoding="utf-8")
for line in fhand:
    nl = nl + 1
    print(nl)
    print(line)
fhand.close()
with open('romeo.txt', encoding="utf-8") as fhand:  # asi no requiere close
    lineas = fhand.readlines()    # Lista con tres variables str
    print(lineas)

