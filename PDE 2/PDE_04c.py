# diccionario de palabras y consecutivo
fname = input("Enter file name: ")
fh = open(fname)
# lst = []
dic1 = dict()
n = 0
for line in fh:
    words1 = line.split()
    for w in words1 :
        if w in dic1 :
         	continue
        n = n + 1
        ns = str(n)
        dic1[w] = ns
# lst.sort()
print(dic1)
"29" in dic1
