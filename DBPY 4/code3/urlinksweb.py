# Do the imports
import bs4 as bs
import urllib 
from urllib import request, error
from urllib.request import urlopen
import collections
collections.Callable = collections.abc.Callable

# source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
#from urllib import request, parse, error
# from bs4 import BeautifulSoup as bs 
import ssl 

# SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

# Ask for user input
#url = input('Enter url\n>> ')
url = 'http://www.dr-chuck.com/page1.htm'
# Check if http:// is in url if not add
if 'http://' not in url:
    url = 'http://'+url

# Get the url
html = urllib.request.urlopen(url).read()
# html = request.urlopen(url, context=ctx).read()

# Parse with BeautifulSoup
soup = bs(html, 'html.parser')

# Get anchor tags
tags = soup('a')

# Loop through and print
for tag in tags:
    print(tag.get('href', None))