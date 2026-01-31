fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("archivo no puede sr abierto o no existe")
    quit()
# lst = list()
for line in fh:
    line = line.rstrip()
    print(line.upper())
    
