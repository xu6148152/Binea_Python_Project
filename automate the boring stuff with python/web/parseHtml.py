#! python3

import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
playFile = open('example.html', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
print(elems)
# type(noStarchSoup)

