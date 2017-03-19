#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen




class TestAddition(unittest.TestCase):
    def setUp(self):
        print("Setting up the test")

    def tearDown(self):
        print("Tearing down the test")

    def test_twoPlusTwo(self):
        total = 2 + 2
        self.assertEqual(4, total)

class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url

        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url), "lxml")
            titles = self.titleMatchURL()
            self.assertEqual(titles[0], titles[1])
            self.assertTrue(self.test_contentExists())
            url = self.getNextLink()
        print("Done")

    def titleMatchsURL(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/")+6):]
        urlTitle = urlTitle.replace("_", "")
        # urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExist(self):
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        if content is not None:
            return True
        return False

    def setUpClass():
        global bsObj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bsObj = BeautifulSoup(urlopen(url), "lxml")

    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("Monty Python", pageTitle)

    def test_contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        self.assertIsNotNone(content)



if __name__ == '__main__':
    unittest.main()