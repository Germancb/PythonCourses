# diccionario de palabras y su conteo
fname = input("Enter file name: ")
fh = open(fname)
# lst = []
dic2 = dict()
for line in fh:
    words1 = line.split()
    for w in words1 :
        dic2[w] = dic2.get(w,0) + 1
# lst.sort()
print(dic2)