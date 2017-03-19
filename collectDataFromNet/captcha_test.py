#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps
import time


def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x < 142 else 255)
    borderImage = ImageOps.expand(image, border=20, fill='white')
    borderImage.save(imagePath)


captchaResponse = ''

while len(captchaResponse) != 5:
    html = urlopen('http://pythonscraping.com/humans-only')
    bsObj = BeautifulSoup(html, "lxml")
    imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"]
    formBuildId = bsObj.find("input", {"name": "form_build_id"})["value"]
    captchaSid = bsObj.find("input", {"name": "captcha_sid"})["value"]
    captchaToken = bsObj.find("input", {"name": "captcha_token"})["value"]

    captchaUrl = "http://pythonscraping.com" + imageLocation
    urlretrieve(captchaUrl, "captcha.jpg")
    cleanImage("captcha.jpg")
    p = subprocess.Popen(["tesseract", "captcha.png", "captcha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("captcha.txt", 'r')

    captchaResponse = f.read().replace(" ", "").replace("\n", "")
    print("Captcha solution attempt: " + captchaResponse)

    if len(captchaResponse) != 5:
        print("There was a problem readering the CAPTCHA correctly!")
    time.sleep(2)

if len(captchaResponse) == 5:
    params = {"captcha_token": captchaToken, "captcha_sid": captchaSid, "form_id": "comment_node_page_form",
              "form_build_id": formBuildId,
              "captcha_response": captchaResponse, "name": "Ryan Mitchell", "subject": "I com to seek the Grail",
              "comment_body[und][0][value]": "...and I am definitely not a bot"}
    r = requests.post("http://www.pythonscraping.com/comment/reply/10", data=params)
    responseObj = BeautifulSoup(r.text, "lxml")
    if responseObj.find("div", {"class": "messages"}) is not None:
        print(responseObj.find("div", {"class": "messages"}).get_text())
