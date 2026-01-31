# assigment 8.4
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words1 = line.split()
    for w in words1 :
        if w in lst :
         	continue 
        lst.append(w)
lst.sort()
print(lst)

