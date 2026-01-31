fh = open("mbox-short.txt")
count = 0
for line in fh :
    count = count + 1
#   print(line)
    line = line.rstrip()
    if line.startswith("From:") :
        print(line)
print(count)
# inp = fh.read()
# print(len(inp))