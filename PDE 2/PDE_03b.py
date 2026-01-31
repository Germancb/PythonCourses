fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("archivo no puede ser abierto o no existe")
    quit()
count = dict()
for line in fh:
    words = line.split()
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
print(count)
    
