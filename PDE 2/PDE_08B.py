name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
mydict = dict()
handle = open(name)
#
for line in handle :
    line = line.rstrip()
    if not line.startswith("From") : continue
    words = line.split()
    w1 = words[0]
    if len(w1) == 5 : continue
    hr1 = words[5]
    print(hr1)
    hr2 = hr1.split(":")
    hr3 = hr2[0]
#   print(hr3)
#   lst.append(wa)
    mydict[hr3] = mydict.get(hr3, 0) + 1
#   print(mydict)
tmp = list()
for k, v in mydict.items() :
    newt = (k, v)
    tmp.append(newt)
tmp = sorted(tmp)
for k, v in tmp :
    print(k, v)
# bigword = None
# bigcount = None
# for kv, value in mydict.items() :
#   print(kv, value)
#    if bigcount is None or value > bigcount :
#      bigword = kv
#      bigcount = value
#
# print(bigword, bigcount)

