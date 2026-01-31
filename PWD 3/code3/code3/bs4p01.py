#from bs4 import BeautifulSoup
# import requests
# se necesita  antes en consola   py -m pip install requests
import bs4 as bs
import urllib 
import requests

x = requests.get('https://w3schools.com')
print(x.status_code)

url = "https://docs.python.org"
result = requests.get(url)

print(result)

#  200    y Response [200)]



