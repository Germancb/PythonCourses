# Ejercico 2 cap 11
import re
fname= input("Entre un nombre de archivo: ")
try:
    data1 = open('mbox-short.txt')
except:
    print("nombre de archivo no válido o no existe", fname)
    exit()
sum = 0
ndatos = 0
nval = str()
for line in data1 :
    nval = re.findall("^X\S*: ([0-9.]+)", line)
#    nval = re.findall('([0-9.]+)', line)
#    nval = re.findall("([0-9].[0-9])", line)
    if len(nval) > 0 :
#        print(nval)
        for i in nval :
            ndatos = ndatos + 1
            sum = sum + float(i)
print(sum)
print(ndatos)
print(sum/ndatos)
