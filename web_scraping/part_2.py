import requests
from bs4 import BeautifulSoup
import csv

# Show only winners and not runner-ups
url = "https://en.wikipedia.org/wiki/United_States_presidential_election"
data = requests.get(url)
soup = BeautifulSoup(data.content, "html.parser")

table = soup.select(".wikitable > tbody > tr")

csv_data = [['order', 'year', 'winner', 'winner electoral votes']]

for rows in table:
    row = rows.select("td")
    if len(row) == 8:
        order = len(csv_data)
        year = row[0].text
        winner = row[2].text
        winner_electoral_votes = row[6].text
        data1 = year.split()
        data2 = winner.split()
        data3 = winner_electoral_votes.split()
        csv_data.append([order, data1[0], " ".join(data2), data3[0]])
    if len(csv_data) == 2:
        csv_data.append([2, 1792, "George Washington", 132])
        csv_data.append([3, 1796, "John Adams", 71])
with open('elections.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
