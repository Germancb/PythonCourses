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
# url = 'http://data.pr4e.org/romeo.txt'
#url = input('Enter - ')
source = urllib.request.urlopen('http://data.pr4e.org/romeo.txt').read()
# html = urllib.request.urlopen(url, context=ctx).read()
soup = bs.BeautifulSoup(source,"html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

c=0
for l in source:
    c= c + 1
print(c)

print(soup.title)
print(soup.get_text())
# corre ok