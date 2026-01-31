text = "X-DSPAM-Confidence:    0.8475"
fpos = len(text)
print(fpos)
pos = text.find("0")
print(pos)
nump = text[pos:fpos]
print(nump)