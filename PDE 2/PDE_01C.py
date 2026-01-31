text = "X-DSPAM-Confidence:     0.8475"
index = 0
while index < len(text) :
    char = text[index]
    if char in(".0123456789") :
        pos = index
        index = len(text)
    else :
        index = index + 1 
print(pos)
