#! python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

key_events = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
try:
    htmlElem = browser.find_element_by_tag_name('body')
    print('find element %s' % str(htmlElem))
    count = 0
    while True:
        gameMessage = browser.find_element_by_xpath("//div[@class='game-message']/p")
        # print('gameMessage ' + gameMessage)
        if gameMessage is not None and len(gameMessage.text) > 0:
            print("game is end")
            break
        event = key_events[count % len(key_events)]
        htmlElem.send_keys(event)
        print('send event %s' % str(event))
        count += 1
        # browser.implicitly_wait(1)
        sleep(3)
except Exception as error:
    # print('can\'t find element')
    print("error" + error)

