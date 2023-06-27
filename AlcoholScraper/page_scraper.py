import bs4
import urllib.request
from requests_html import HTMLSession



link = input()
s = HTMLSession()
response = s.get(link)
response.html.render()

print(response)

# source = urllib.request.urlopen(link).read()

# soup = bs4.BeautifulSoup(source,'html.parser')
# print(soup.find('div', class_='CoveoResultList'))
# print(soup.find('div', class_='CoveoResultList'))
# count = 0
# for drink in soup.find_all('div', class_='coveo_card_layout'):
#     if count > 0:
#         break
#     count +=1
#     print(drink)

