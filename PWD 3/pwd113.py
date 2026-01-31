import re
hand = open("mbox-short.txt")
sum = 0
ndatos = 0
for line in hand:
    line = line.rstrip()
#   x = re.findall("^X\S*: ([0-9.]+)", line)
    x = re.findall("^New Revision: ([0-9.]+)", line)
    if len(x) > 0:
        print(x)
        for i in x:
            print(i)
            sum = sum + float(i)
            ndatos = ndatos + 1
print(sum)
print(int(sum/ndatos))