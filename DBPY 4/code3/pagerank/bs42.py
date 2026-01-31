from bs4 import BeautifulSoup
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# url=input('Enter- ')
# req_file=urllib.request.urlopen(url).read()
soup=BeautifulSoup(source,"html.parser")

print(soup.prettify())

# si corre