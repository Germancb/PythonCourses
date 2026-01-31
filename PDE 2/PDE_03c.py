fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("archivo no puede sr abierto o no existe")
    quit()
count = dict()
for line in fh:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0)  + 1        
print(count)

for key in count:
    print(key, count[key])
    
