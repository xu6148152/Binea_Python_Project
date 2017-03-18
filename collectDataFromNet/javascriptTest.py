#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


def selenium_test1():
    driver = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    time.sleep(3)
    print(driver.find_element_by_id('content').text)
    driver.close()


def selenium_test2():
    driver = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')
    driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID))
    finally:
        print(driver.find_element_by_id("content").text)
        driver.close()


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem = driver.find_element_by_tag_name('html')
        except StaleElementReferenceException:
            return


def test_waitforload():
    driver = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')
    driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
    waitForLoad(driver)
    print(driver.page_source)


if __name__ == '__main__':
    test_waitforload()