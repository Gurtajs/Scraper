
import pip._vendor.requests as requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/forms/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

wins = soup.select("tr th:nth-of-type(6)")

for win in wins:
  print(win.text+':')
win_percentage = soup.find_all("td", class_="pct text-success")


for percentage in win_percentage:
  print(percentage.text) 
