import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"
data = requests.get(url)
soup = BeautifulSoup(data.content, "html.parser")

titles = soup.select("h3", class_=".ipQwMb ekueJc RD0gLb")
for title in titles:
    headline = title.select_one("a")
    print(headline.text.strip(), end="\n" * 2)

def find_headline_by_keyword(hdline, keyword):
    for headline in hdline:
        headline.find_all("a")
        if keyword.lower() in headline.text.lower():
            return headline.text.strip()

print(find_headline_by_keyword(titles, "bezos"))
