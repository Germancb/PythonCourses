# accesando web pages urlib
import urllib.request, urllib.parse, urllib.error
fhand= urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
contador =dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        contador[word] = contador.get(word, 0) + 1
print(contador)