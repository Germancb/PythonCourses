import bs4 as bs
import urllib 
from urllib.request import urlopen
import collections
collections.Callable = collections.abc.Callable

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
c=0
for l in source:
    c= c + 1
print(c)

soup = bs.BeautifulSoup(source,"html.parser")
print(soup.title)
# print(soup.get_text())
# corre ok




