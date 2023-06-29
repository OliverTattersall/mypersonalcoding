from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Drink
from .forms import TestForm, SearchForm
from django.shortcuts import render
import bs4
import urllib.request
from django.template.defaulttags import register

drink_mapper = {'beer': 'Beer', 'hardliquor': 'Hard liquor', 'wine': 'Wine', 'coolers': 'Coolers','ipas': 'IPAs', 'all':'All Drinks', 'ciders':'Ciders'}

def return_facts_beer_store(link):
    if Drink.objects.filter(link=link).exists():
        print('\nAlready Exists\n')
        return False
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
        # print(val)


    return vals


def return_facts_lcbo(link):
    if Drink.objects.filter(link=link).exists():
        print('\nAlready Exists\n')
        return False
    try:
        source = urllib.request.urlopen(link).read()
        soup = bs4.BeautifulSoup(source,'html.parser')

        # for res in soup.find_all('div', class_='lcbo-product-size'):
        #     print(res)
        name = soup.find('span', class_='base').get_text()
        
        units = 1
        volume_text = soup.find('div', class_='lcbo-product-size').get_text()
        if ' x ' in volume_text:
            volume = int(volume_text.split()[2])
            units = int(volume_text.split()[0])
        else:
            volume = int(volume_text.split()[0])
        price_query = soup.find_all('span', class_='price')
        if (len(price_query) > 1):
            good = list(filter(lambda x : 'Original Price' in x.get_text(), price_query))
            price = float(good[0].get_text().replace('$', '').replace('Original Price', ''))
        else:
            price = float(price_query[0].get_text().replace('$', ''))
        alc_perc = float(soup.find('div', class_='moredetail').ul.li.find('div', class_='value').get_text().replace("%",''))/100

        # print(name, units, volume, price, alc_perc)
        return [[name, units, volume, price, alc_perc, False]]
    except:
        return False

    



def get_drink(request, name):

    val = Drink.objects.values().get(name = name)
    return JsonResponse(val, safe=False)
    # return HttpResponse( data , content_type="application/json")

def get_drink_class(request, type):
    queries = request.GET
    
    # print()
    if(type=='all'):
        data = Drink.objects.values()
    else:
        data = Drink.objects.values().filter(type = type)

    if 'store' in queries:
        data = data.filter(store = queries['store'])
    if 'units' in  queries:
        data = data.filter(units = queries['units'])

    if 'min_apd' in queries:
        data  = data.filter(alc_per_dol__gt=queries['min_apd'])

    # print(queries, 'drink' in queries)



    data = list(data)
    data.sort(reverse=True, key=lambda val : val['alc_per_dol'])
    for row in data:
        row['type'] = drink_mapper[row['type']]
    # print(data)

    dictData = {'drinks':data, 'type': drink_mapper[type]}
    return render(request, 'drinksData/drinktable.html', context=dictData )
    # return JsonResponse(data, safe=False)

def submit_values(link, type, store, facts):
    name, units, volume, price, content, sale_price = facts
    send = Drink(name=name, 
                         units = units, 
                         volume = volume, 
                         content = content, 
                         price = price, 
                         tvolume = units*volume,
                         talc = units*volume*content,
                         alc_per_dol = units*volume*content/price,
                         link = link,
                         type = type,
                         store = store,
                         sale_price = sale_price if sale_price else None
                         )
    send.save()

def submit_drink(request):
    form = TestForm( request.POST or None)
    data = "None"
    success = ""
    if form.is_valid():
        data = form.cleaned_data
        print(data)
        link = data['link']
        type = data['type']
        store = data['store']
        success = "Success"
        if store == 'LCBO':
            result = return_facts_lcbo(link)
        else:
            result = return_facts_beer_store(link)
        if result:
            for row in result:
                submit_values(link, type, store, row)
        else:
            success="Success: Link did not work. Product could already be in database or the link is badly formatted."
    return render(request,'drinksData/forms.html', {'form': form, 'success':success})

def heinekendex(request):
    data = Drink.objects.values().filter(type = 'beer').filter(store='LCBO')
    heineken = Drink.objects.values().get(name='Heineken', units=6)

    hprice = heineken['price']
    hvolume = heineken['volume']
    hcontent = heineken['content']

    # print(heineken)
    data = list(data)
    data.sort(reverse=True, key=lambda val : val['alc_per_dol'])
    data_numbers = list(map(lambda val:val['alc_per_dol']*hprice/(hvolume*hcontent), data))
    data_labels  = list(map(lambda val:val['name'], data))
    return render(request, 'drinksData/heinekendex.html', {'data_numbers':data_numbers, 'data_labels':data_labels})


def index(request):
    form = SearchForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        # print(data, type(data))
        type = data['type']
        # store = data['store']
        # units = data['units']
        # min_apd = data['min_apd']
        queries = []
        for key,val in data.items():
            # print(key, val)
            if val and key!='type':
                print(key)
                queries.append(key + '='+str(val))
        path = '/many/'+type+'/?' + '&'.join(queries)
        print(path)
        return HttpResponseRedirect(path)

    return render(request, 'drinksData/index.html', {'form':form})


@register.filter(name="multiply")
def multiply(value, arg):
    return value*arg