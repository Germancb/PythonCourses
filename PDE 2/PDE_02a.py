fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    count = count + 1
# fhm = fh.read()
#    line = line.rstrip()count = count + 1
print("Numero lineas ", count)
