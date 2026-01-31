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

from urllib.request import urlopen
# url = "https://www.pythonforbeginners.com"
url = "http://www.dr-chuck.com/page1.htm"

# content = urlopen(url).read()
source = urllib.request.urlopen(url, context=ctx).read()
soup = bs.BeautifulSoup(source,"html.parser")
# soup = BeautifulSoup(content, "html.parser")

print(soup.prettify())

# corre ok