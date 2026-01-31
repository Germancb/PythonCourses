# assigment 8.4
import string
fname = input("Enter file name: ")
try:
    fh=open(fname)
except:
    print('No es posible abrir el archivo: ')
    exit()
cont1=dict()

for line in fh:
    words1 = line.rsplit()
    line =line.translate(line.maketrans('', '', string.punctuation))
    line =line.lower()
    words=line.split()
    for w in words1 :
        if w not in cont1:
         	cont1[w]  = 1
        else:
            cont1[w] + 1 
        
print(cont1)

