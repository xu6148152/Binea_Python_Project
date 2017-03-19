#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import unittest


class TestAddition(unittest.TestCase):
    driver = None

    def setUp(self):
        global driver
        driver = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')
        url = "http://pythonscraping.com/pages/javascript/draggableDemo.html"
        driver.get(url)

    def tearDown(self):
        print("Tearing down the test")

    def test_drag(self):
        global driver

        element = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("div2")
        actions = ActionChains(driver)
        actions.drag_and_drop(element, target).perform()

        self.assertEqual("You are definitely not a bot!", driver.find_element_by_id("message").text)


def selenium_autotest():
    firstnameField = driver.find_element_by_name("firstname")
    lastnameField = driver.find_element_by_name("lastname")
    submitButton = driver.find_element_by_id("submit")

    # 1
    # firstnameField.send_keys("Ryan")
    # lastnameField.send_keys("Mitchell")
    # submitButton.click()

    # 2
    url = "http://pythonscraping.com/pages/files/form.html"
    actions = ActionChains(driver).click(firstnameField).send_keys("Ryan").click(lastnameField).send_keys(
        "Mitchell").send_keys(Keys.RETURN)
    actions.perform()

    print(driver.find_element_by_tag_name("body").text)

    print(driver.find_element_by_id("message").text)

    driver.get_screenshot_as_file('pythonscraping.png')

    driver.close()


if __name__ == '__main__':
    selenium_autotest()
