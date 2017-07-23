from bs4 import BeautifulSoup
import requests

url = "http://www.churchill-society-london.org.uk/Locusts.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

text = soup.get_text()
print(text)
#lines = (line.strip() for line in text.splitlines())
#print