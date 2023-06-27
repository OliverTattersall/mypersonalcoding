import bs4
import urllib.request
import pandas as pd
import openpyxl


def return_facts(link):
    try:
        source = urllib.request.urlopen(link).read()
    except:
        return False

    soup = bs4.BeautifulSoup(source,'html.parser')

    # for res in soup.find_all('div', class_='lcbo-product-size'):
    #     print(res)
    name = soup.find('span', class_='base').get_text()
    units = 1
    volume_text = soup.find('div', class_='lcbo-product-size').get_text()
    if 'x' in volume_text:
        volume = volume_text.split()[2]
        units = volume_text.split()[0]
    else:
        volume = volume_text.split()[0]
    price = soup.find('span', class_='price').get_text()
    alc_perc = soup.find('div', class_='moredetail').ul.li.find('div', class_='value').get_text()

    print(name, units, volume, price, alc_perc)
    return [name, units, volume, price, alc_perc]



def main():
    df = pd.read_excel(r'AlcoholScraper\drinks.xlsx')
    link = input()
    while link !='n':
        facts = return_facts(link)
        link = input()
    return True
# main()
# df = pd.read_excel(r'AlcoholScraper\drinks.xlsx')

# print(df)