##############################################
# YOU WERE THINKING OF MOVING THINGS TO FUCNTIONS LIKE A READFILE FUNCTION AND A CHECK IF NEW FUNCTION
##############################################
from bs4 import BeautifulSoup as soup
#from apschedule.schedulers.blocking import BlockingSchedule
import requests
import schedule
import time
import pandas as pd
import json
import csv


url = requests.get(
    'https://store.playstation.com/en-us/grid/STORE-MSF77008-NEWGAMESGRID/1').text
gameTitle = 'gameTitles.txt'
google = 'https://www.google.com/search?q='
psStore = 'https://store.playstation.com/en-us/grid/search-game/1?query='


def getPsGames():
    b_soup = soup(url, 'lxml')
    titles = b_soup.findAll('div', {'class': 'grid-cell__title'})
    allPrices = b_soup.findAll(
        'div', {'class': '__shared-presentation__price-display__900cc'})

    pastGames = getPastTitles()
    print(pastGames)

    filename = 'newGames.csv'
    f = open(filename, 'w', encoding='utf-8')
    headers = "Title, Price, Newly Added?, Search, PS Store\n"
    f.write(headers)

    for i in range(0, len(titles)):
        price = allPrices[i].h3.text
        gameTitle = titles[i].span.text
        realTitle = gameTitle.replace(",", " ")
        if(checkIfNew(pastGames, titles[i].text.strip()) == True):
            f.write(gameTitle.replace(",", " ") +
                    ',' + price + ',' + 'new' + ',' + (google + realTitle.replace(" ", "+")) + ',' + (psStore + realTitle.replace(" ", "%20")) + '\n')
        else:
            f.write(gameTitle.replace(",", " ") +
                    ',' + price + ',' + "-" + ',' + (google + realTitle.replace(" ", "+")) + ',' + (psStore + realTitle.replace(" ", "%20")) + '\n')
        print(gameTitle)
        print(price)
        print()
    f.close()
    getCurrentTitles(titles)
    csvToJson()
    # print(page_soup)
    # print(b_soup.prettify())
    # print(price)


# schedule.every().tuesday.at('15:25').do(psGames)


# while 1:
    # schedule.run_pending()
    # time.sleep(1)
def checkIfNew(pastNewGames, title):
    if(len(pastNewGames) == 0):
        return True
    j = 0
    if title in pastNewGames:
        return False
    else:
        return True


def getPastTitles():
    games = []
    with open(gameTitle, 'r', encoding='utf-8') as reader:
        titlesInFile = reader.readlines()
        for title in titlesInFile:
            games.append(title.strip())
        reader.close()
        return games


def getCurrentTitles(titles):
    file = open('gameTitles.txt', 'w', encoding='utf-8')
    for title in titles:
        file.write(title.span.text + '\n')
    file.close()


def csvToJson():
    csvFile = open('newGames.csv', 'r')
    jsonFile = open('newGames.json', 'w')

    fields = ('Title', 'Price', 'Newly Added')
    reader = csv.DictReader(csvFile, fields)
    for row in reader:
        json.dump(row, jsonFile)
        jsonFile.write('\n')


if __name__ == "__main__":
    getPsGames()
