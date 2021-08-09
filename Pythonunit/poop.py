import requests
import json
import pprint
 

def writeHTML(datajson):
    myfile = open("exampleapi.html","w")
    myfile.write("<!DOCTYPE HTML><html><head></head><body><script src=" 'https://cdn.jsdelivr.net/npm/chart.js@2.8.0' "></script><script src=" 'https://canvasjs.com/assets/script/canvasjs.min.js' "></script><script>var ctx = document.getElementById('chartjs-0').getContext('2d');var chart = new Chart(ctx, {type: 'bar',data: {labels: [")
    for i in range(len(datajson['cryptocurrenciesList'])):
        if i !=0:
            myfile.write("," + datajson['cryptocurrenciesList'][i]['ticker'])
        else:
            myfile.write(datajson['cryptocurrenciesList'][i]['ticker'])
    myfile.write("],datasets: [{label: 'Stock Price',data: [")
    for i in range(len(datajson['cryptocurrenciesList'])):
        if i !=0:
            myfile.write("," + datajson['cryptocurrenciesList'][i]['price'])
        else:
            myfile.write(datajson['cryptocurrenciesList'][i]['price'])
    myfile.write("],pointRadius:0}]},options: {}});</script></body></html>")
    
    myfile.close()
def main():
	response = requests.get("https://financialmodelingprep.com/api/v3/cryptocurrencies")
	
	if (response.status_code == 200):
		datajson = response.json()
        writeHTML(datajson)

main()