from django.http import HttpResponse, JsonResponse
from .models import Drink
from .forms import TestForm
from django.shortcuts import render
# from ./../../scripts/single_scraper.py import return_facts
import bs4
import urllib.request

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
        volume = int(volume_text.split()[2])
        units = int(volume_text.split()[0])
    else:
        volume = int(volume_text.split()[0])
    price = float(soup.find('span', class_='price').get_text().replace('$', ''))
    alc_perc = float(soup.find('div', class_='moredetail').ul.li.find('div', class_='value').get_text().replace("%",''))/100

    # print(name, units, volume, price, alc_perc)
    return [name, units, volume, price, alc_perc]



def get_drink(request, name):

    val = Drink.objects.values().get(name = name)
    return JsonResponse(val, safe=False)
    # return HttpResponse( data , content_type="application/json")

def get_drink_class(request, type):
    data = list(Drink.objects.values().filter(type = type))
    dictData = {'drinks':data}
    return render(request, 'drinksData/drinktable.html', context=dictData )
    # return JsonResponse(data, safe=False)

def submit_drink(request):
    form = TestForm( request.POST or None)
    data = "None"
    if form.is_valid():
        data = form.cleaned_data
        link = data['link']
        type = data['type']
        result = return_facts(link)
        if result:
            print(result)
            print(data, link)
            name = result[0]
            units = result[1]
            volume = result[2]
            price = result[3]
            content = result[4]
            send = Drink(name=name, 
                         units = units, 
                         volume = volume, 
                         content = content, 
                         price = price, 
                         tvolume = units*volume,
                         talc = units*volume*content,
                         alc_per_dol = units*volume*content/price,
                         link = link,
                         type = type
                         )
            send.save()
    return render(request,'drinksData/forms.html', {'form': form})
