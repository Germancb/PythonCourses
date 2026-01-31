text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0.")
print(pos)
fpos= len(text)
print(fpos)
numv= text[pos:fpos]
print(numv)