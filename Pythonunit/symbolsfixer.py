import json
import requests
import webbrowser


def deletestock(a):
    print(a)
    myfile=open("stocksymbols.json","r")
    symbol=myfile.read()
    stuff=json.loads(symbol)
    for i in range(len(stuff)):
        if a==stuff[i]['Symbol']:
            stuff.remove(stuff[i])
            break
    stuffstr=json.dumps(stuff)
    myfile.close()
    myfile=open("stocksymbols.json",'w')
    myfile.write(stuffstr)
    myfile.close()




myfile=open("stocksymbols.json","r")
symbol=myfile.read()
stuff=json.loads(symbol)
for i in range(len(stuff)):
    try:
        r=requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol="+ stuff[i]['Symbol'] + "&api_token=wDlGeK1dKNkRmKknWMEyMXmFAHeqddSElO07Th6uqZy5Qx1bMMuZmGdrrtQE")
        datajson=r.json()
        v=datajson['data'][0]['price']
    except:
        deletestock(stuff[i])

myfile.close()





