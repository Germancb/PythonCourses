# ejercicioo  3cap 9
# Assigmnet 10.2
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
mydict = dict()
handle = open(name)
#
for line in handle :
    print(line)
#   line = line.rstrip()
    if not line.startswith("From") : continue
    words = line.split()
    if words[0] == "From:": continue
#   print(words)
    wa = words[1]
    # print(wa)
#   lst.append(wa)
    mydict[wa] = mydict.get(wa, 0) + 1
# (mydict)
