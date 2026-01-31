fname = input("Enter file name: ")
fh = open(fname)
# lst = list()
for line in fh:
    line = line.rstrip()
    print(line.upper())
