from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import csv


START = 'https://pl.wikipedia.org/wiki/Lista_laureat%C3%B3w_Nagrody_Nobla'
LANGUAGES = ['en','de','sv','it','nl','fi']
data = './data.csv'

def addToCSV(csvfile,row):
    with open(csvfile, 'a+') as fp:
        filewriter = csv.writer(fp, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(row)

def getLang(page):
    return page[8:10]

def getUrls(table):
    urls = list()

    return urls

def createUrls(endings):
    urls = list()
    for lang in LANGUAGES:
        for end in endings:
            tmp = 'https://'+lang+'.wikipedia.org'+end+''
            urls.append(tmp)
    return urls

def getPageContent(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return ''
    except URLError as e:
        print(e)
        return ''
    else:
        return html.read()   

def parseHtml(page):
    return BeautifulSoup(page,'html.parser')

def getAtributeData(what,soup):
    try:
        return soup.findAll(what)
    except:
        return ''
def main():
    mainContent = getPageContent(START)
    if(mainContent):
        soup = parseHtml(mainContent)
    else:
        print("no page to show")

    elements = getAtributeData('tbody',soup) 
    urlEnding = list()
    if elements:
        for element in elements:
            tmp = getAtributeData('a',element)
            for t in tmp:
                try:
                    urlEnding.append(t.attrs['href'])
                except:
                    continue
    if urlEnding:
        urls = createUrls(urlEnding)
        #start csv
        addToCSV(data,['language','text'])
        for page in urls:
            tmp = getPageContent(page)
            if tmp:
                html = parseHtml(tmp)
            else:
                continue

  
            if html:
                list_of_paragraphs=getAtributeData('p',html)
                
                if list_of_paragraphs:
                    for par in list_of_paragraphs:
                        lang = getLang(page)                        
                        text = par.get_text()
                        row = [lang,text]
                        addToCSV(data,row)



if __name__=="__main__":
    main()