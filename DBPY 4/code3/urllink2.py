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

# url = input('Enter - ')
url=('http://www.dr-chuck.com/page1.htm')
source = urllib.request.urlopen(url).read()
# html = urllib.request.urlopen(url, context=ctx).read()
soup = bs.BeautifulSoup(source,"html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

# corre ok
