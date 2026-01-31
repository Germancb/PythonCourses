
# Assigment 8.5
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
# lst = list()
fh = open(fname)
count = 0
for line in fh :
    line = line.rstrip()
    if not line.startswith("From:") : continue
    words = line.split()
    wa = words[1]
    print(wa)
    count = count + 1
#
print('There were:',count, 'Lines in the file with From as the firs word')

