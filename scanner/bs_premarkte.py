import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market").read()
soup = BeautifulSoup(url)

for line in soup.find_all('a'):
    print(line.get('href'))
