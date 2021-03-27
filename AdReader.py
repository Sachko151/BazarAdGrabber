import requests
from bs4 import BeautifulSoup


def printAd(url):
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
