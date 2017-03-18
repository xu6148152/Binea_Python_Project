import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import datetime
import random

random.seed(datetime.datetime.now())

pages = set()

allExtLinks = set()
allIntLinks = set()

# get all inner site
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # findl all start with '/' link
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# get all external site
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # find all start with 'http' or 'www' and exclude current link
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = requests.get(startingPage)
    bsObj = BeautifulSoup(html.content, "lxml")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def getNextExternalLink(link):
    rootLink = "http://oreilly.com"
    html = requests.get(rootLink + link)
    bsObj = BeautifulSoup(html.content, "lxml")
    externalLinks = getExternalLinks(bsObj, html)
    if len(externalLinks) == 0:
        return rootLink
    return externalLinks[random.randint(0, len(externalLinks) - 1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("random external site:" + externalLink)
    followExternalOnly(externalLink)

def getAllExternalLinks(siteUrl):
    html = requests.get(siteUrl)
    bsObj = BeautifulSoup(html.content, "lxml")
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)

    for link in internalLinks:
        if link not in allIntLinks:
            print(link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

def test_reg_BeautifulSoup():
    html = requests.get('http://www.pythonscraping.com/pages/page3.html')
    # html = urlopen('http://www.pythonscraping.com/pages/page3.html')
    bsObj = BeautifulSoup(html.content)
    reg = "\.\.\/img\/gifts/img.*\.jpg"
    images = bsObj.findall("img", {"src": re.compile(reg)})
    for image in images:
        print(image["src"])


def test_wiki_data():
    html = requests.get('http://en.wikipedia.org/wiki/Kevin_Bacon')
    bsObj = BeautifulSoup(html.content, "lxml")
    # for link in bsObj.findAll("a"):
    for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def getLinks(articleUrl):
    global pages
    html = requests.get('http://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html.content, "lxml")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("lack some attribute")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
                # return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


def test_getLinks():
    # links = getLinks("/wiki/Kevin_Bacon")
    # while len(links) > 0:
    #     newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    #     print(newArticle)
    #     links = getLinks(newArticle)

    getLinks("")


def test_followExternalOnly():
    followExternalOnly("http://oreilly.com")

def test_utf8_encode():
    textPage = requests.get("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
    print(str(textPage.content), 'utf-8')


if __name__ == '__main__':
    test_utf8_encode()