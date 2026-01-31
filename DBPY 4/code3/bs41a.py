import bs4 as bs
import urllib 
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url= 'https://pythonprogramming.net/parsememcparseface/'
html = urlopen(url, context=ctx).read()
# source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
c=0
for l in html:
    c=c+1
print(c)
#soup = bs.BeautifulSoup(source,'lxml')
# print(soup.title)
# print(soup.get_text())




