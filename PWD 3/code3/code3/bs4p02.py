from bs4 import BeautifulSoup
import requests
import urllib2
from urllib.request import urlopen
import collections
collections.Callable = collections.abc.Callable
# corre con el url dos

# url = "www.pythonforbeginners.com"

url = 'https://docs.python.org/3/'
result = requests.get("http://" +url)
data = result.text
content = urlopen(url).read()

soup = BeautifulSoup(content, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))