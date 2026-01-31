text = "X-DSPAM-Confidence:    0.8475"
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
valueav = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    posi = line.find("0.")
    posf = posi + 6
    numbers = line[posi : posf]
    number = float(numbers)    
    if valueav == 0 :
        valueav = number
        count = 1
    else :
        count = count + 1
        valueav = (valueav + number)/count     
print("Average spam confidence;", valueav)
