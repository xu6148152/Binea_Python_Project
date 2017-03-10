from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
type(browser)
browser.get('http:inventwithpython.com')
try:
    # elem = browser.find_element_by_class_name('bookcover')
    # linkElem = browser.find_element_by_link_text('Read It Online')
    htmlElem = browser.find_elements_by_tag_name('html')
    htmlElem.send_keys(Keys.END)
    htmlElem.send_keys(Keys.HOME)
    # type(linkElem)
    # linkElem.click()
    
    # print('Found <%s> element with that class name!' %(elem.tag.name))
except:
    print('Was not able to find an element with that name')
