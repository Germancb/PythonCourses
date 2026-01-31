fname = input("Enter file name: ")
fh = open(fname)
#  = 0
# for line in fh:
#    count = count + 1
fhm = fh.read()
#    line = line.rstrip()
print("Numero lineascaracters ", len(fhm))
print("Primeros 20 caracteres ", fhm[:20])
