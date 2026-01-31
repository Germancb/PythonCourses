# Assigmnet 10.2
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
mydict = dict()
handle = open(name)
#
for line in handle :
    line = line.rstrip()
    if not line.startswith("From:") : continue
    words = line.split()
    wa = words[1]
#   print(wa)
#   lst.append(wa)
    mydict[wa] = mydict.get(wa, 0) + 1
bigword = None
bigcount = None
for kv, value in mydict.items() :
#   print(kv, value)
    if bigcount is None or value > bigcount :
       bigword = kv
       bigcount = value
#
print(bigword, bigcount)