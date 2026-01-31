import re
data1 = open('regex_sum_1486143.txt')
sum = 0
ndatos = 0
nlist = list()
for line in data1 :
    nlist = re.findall('[0-9]+', line)
#   print(nlist)
    leg = len(nlist)
#   print(leg)
    if leg > 0 :
        for i in nlist :
            y1 = float(i)
            ndatos = ndatos + 1
            sum = sum + y1
#            print(sum)
print(sum)
print(ndatos)
