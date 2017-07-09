import urllib
from bs4 import BeautifulSoup

url = "http://www.churchill-society-london.org.uk/Locusts.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

text = soup.get_text()
print(text)
#lines = (line.strip() for line in text.splitlines())
#print