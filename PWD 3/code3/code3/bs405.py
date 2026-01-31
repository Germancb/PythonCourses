import bs4 as bs
import requests
import collections
collections.Callable = collections.abc.Callable

#url = raw_input("Enter a website to extract the URL's from: ")
url = 'https://docs.python.org/3/'
r  = requests.get(url)

data = r.text

# soup = BeautifulSoup(data)
soup = bs.BeautifulSoup(data,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

# corre ok