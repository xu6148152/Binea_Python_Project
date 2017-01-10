#! python3

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
print(res.text)
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result
linkElems = soup.select('.t a')
print(len(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://baidu.com' + linkElems[i].get('href'))