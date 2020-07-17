##############################################
#YOU WERE THINKING OF MOVING THINGS TO FUCNTIONS LIKE A READFILE FUNCTION AND A CHECK IF NEW FUNCTION
##############################################
from bs4 import BeautifulSoup as soup
#from apschedule.schedulers.blocking import BlockingSchedule
import requests
import schedule
import time


def psGames():
    pastNewGames = []
    url = requests.get('https://store.playstation.com/en-us/grid/STORE-MSF77008-NEWGAMESGRID/1').text

    gameTitle = 'gameTitles.txt'
    with open(gameTitle, 'r', encoding='utf-8') as reader:
        titlesInFile = reader.readlines()
        for title in titlesInFile:
            pastNewGames.append(title.strip())
        print(pastNewGames)
        reader.close()

    file = open(gameTitle, 'w', encoding='utf-8')


    filename = 'newGames.csv'
    f = open(filename,'w', encoding='utf-8')
    headers = "title, price\n"
    f.write(headers)

    b_soup = soup(url, 'lxml')
    titles = b_soup.findAll('div', {'class':'grid-cell__title'})
    allPrices = b_soup.findAll('div', {'class':'__shared-presentation__price-display__900cc'})

    for i in range(0, len(titles)):
        price = allPrices[i].h3.text
        gameTitle = titles[i].span.text
        print(gameTitle)
        print(price)
        file.write(gameTitle + '\n')
        f.write(gameTitle.replace(","," ") + ',' + price + '\n')
    f.close()
    file.close()
    #print(page_soup)
    #print(b_soup.prettify())
    #print(price)


#schedule.every().tuesday.at('15:25').do(psGames)


#while 1:
    #schedule.run_pending()
    #time.sleep(1)


if __name__ == "__main__":
    psGames()