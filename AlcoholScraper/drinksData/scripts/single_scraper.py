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

def return_facts_beer_store(link):
    # if Drink.objects.filter(link=link).exists():
    #     print('\nAlready Exists\n')
    #     return False
    try:
        req = urllib.request.Request(url=link, headers={'User-Agent': 'Mozilla/5.0'})
        source = urllib.request.urlopen(req).read()
    except:
        print('error')
        return False
    
    soup = bs4.BeautifulSoup(source,'html.parser')
    name = soup.find('h1', class_="capitalize").get_text()
    content = float(soup.find('div', class_="ABV").find('p', class_="details-value").get_text().replace("%", ''))/100
    vals = [] #[name, units, volume, price, content, sale_price]
    options = soup.find_all('div', class_='availablecases_addtocart')
    for option in options:
        price = option.find('div', class_='price').get_text().replace('\n', '')
        sale_price = False
        if 'Sale' in price:
            price = price.split(' ')
            sale_price = float(price[1].replace('$', ''))
            price = float(price[0].replace('$', ''))
        else:
            price = float(price.replace('$', ''))
        
        quantity = option.find('div', class_='quantity').get_text().replace('\n', '').split("PACKUP")[0].strip()
        # print(quantity)
        units = 1
        if 'X' in quantity:
            quantity = quantity.split(' ')
            units = int(quantity[0])
            
            if 'L' in quantity[4]:
                volume = int(float(quantity[3])*1000)
            else:
                volume = int(quantity[3])
        else:
            quantity = quantity.split(' ')
            if 'L' in quantity[1]:
                volume = int(float(quantity[0])*1000)
            else:
                volume = int(quantity[0])
        # print(units, volume)

        val = [name, units, volume, price, content, sale_price]
        vals.append(val)
        print(val)


    return vals

def main():
    # df = pd.read_excel(r'AlcoholScraper\drinks.xlsx')
    link = input()
    while link !='n':
        # facts = return_facts(link)
        facts = return_facts_beer_store(link)

        link = input()
    return True
main()
# df = pd.read_excel(r'AlcoholScraper\drinks.xlsx')

# print(df)