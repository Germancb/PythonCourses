import bs4 as bs
import urllib
from urllib.request import urlopen
import collections
collections.Callable = collections.abc.Callable
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = "https://www.pythonforbeginners.com"

url = 'https://docs.python.org/3/'
source = urllib.request.urlopen(url, context=ctx).read()
soup = bs.BeautifulSoup(source,"html.parser")
c=0
for l in source:
    c= c + 1
print(c)

for link in soup.find_all('a'):
    print(link.get('href'))
# corre ok