from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pythonscraping.com/pages/page1.html")
html = BeautifulSoup(html, "html.parser")
try:
    print(html.h1.text)
except AttributeError:
    print("tag does not exists")