# задание 2
import requests

# print(requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text)

def currency_rates(x):
    sait = requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text
    if x in sait:
        x = sait[sait.find('<Value>', sait.find(x)) + 7:sait.find('</Value>', sait.find(x))]
        print(x)
    elif x not in sait:
        print(None)
currency_rates('USD')
currency_rates('EUR')
