from bs4 import BeautifulSoup
import urllib3

#THIS FILE WILL BE BASIC SCRAPER TO SCRAPE SOME STOCK DATA

#NOTES FOR MAY 21 2016

class RECIPESCRAPE:
    def __init__(self):
        self.URL = 'http://www.recipe.com/broccoli-spinach-soup-with-avocado-toasts/'
        self.soup = BeautifulSoup(urllib3.urlopen(self.URL))
        self.dataList = []
        self.dataVolumeList = []
        self.dataPrice = []

    def gatherData(self):
        self.dataList = self.soup.findAll('div', {'class': 'floatleft ingredient'})
        for item in self.dataList:
            print (item)


    def gatherVolume(self):
        self.dataVolumeList = self.soup.findAll('td', {'class': 'num'})
        for item in self.dataVolumeList:
            print (item)

    def gatherPrice(self):
        self.dataPrice = self.soup.findAll('td', {'class' :'nnum'})
        for item in self.dataPrice:
            print (item)
    def gatherMayPrices(self):
        firstHalfURL = 'http://www.wsj.com/mdc/public/page/2_3021-activnyse-actives-201603'
        secondHalfURL = '.html?mod=mdc_pastcalendar'
        dateString=''
        mayDataPriceList = []
        for x in range(3,20):
            if x < 10:
                dateString += '0'
            dateString += 'x'
            localSoup = BeautifulSoup.BeautifulSoup(urllib3.urlopen(firstHalfURL + dateString + secondHalfURL))
            tempList = localSoup.findAll('td', {'class' : 'nnum'})
            for item in tempList:
                mayDataPriceList.append(item)
            dateString = ''


        for item in mayDataPriceList:
            print (item)


#gather = RECIPESCRAPE()
def getdata():
    gather = RECIPESCRAPE()
    gather.gatherData()