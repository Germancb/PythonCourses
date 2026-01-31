text = "X-DSPAM-Confidence:    0.8475"
fpos = len(text)
pos = text.find("0")
ipos = float(pos)
nump = text[pos : fpos]
print(ipos)
print(nump)