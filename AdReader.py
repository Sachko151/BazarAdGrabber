import requests
from bs4 import BeautifulSoup


def printAdBazar(url):
    html_doc2 = requests.get(url).text
    soup = BeautifulSoup(html_doc2, 'html.parser')
    adName = soup.find('h1', {'class': 'adName'}).text
    cityLocation = soup.find('span', {'class': 'location'}).text
    adDescription = soup.find('div', {'class': 'clearfix text show-more-height'}).text
    adPrice = soup.find('span', {'class': 'price'}).text
    print("========================================================================")
    print(adName.replace(" ", ""))
    print(cityLocation.replace(" ", ""))
    adDescriptionList = adDescription.split(" ")
    for i in range(len(adDescriptionList)):
        if (i % 20 == 0):
            print()
        print(adDescriptionList[i], end=" ")
    print("\n  Цена: " + adPrice)
    print("========================================================================")

def printAdOlx(url):
    html_doc2 = requests.get(url).text
    soup = BeautifulSoup(html_doc2, 'html.parser')
    adName = soup.find('h1', {'class': 'css-1oarkq2-Text eu5v0x0'}).text
    adOwner = soup.find('h2', {'class': 'css-owpmn2-Text eu5v0x0'}).text
    adDescription = soup.find('div', {'class': 'css-g5mtbi-Text'}).text
    adPrice = soup.find('h3', {'class': 'css-8kqr5l-Text eu5v0x0'}).text
    print("========================================================================")
    print(adName.replace(" ", ""))
    print(adOwner.replace(" ", ""))
    adDescriptionList = adDescription.split(" ")
    for i in range(len(adDescriptionList)):
        if (i % 20 == 0):
            print()
        print(adDescriptionList[i], end=" ")
    print("\n  Цена: " + adPrice)
    print("========================================================================")
