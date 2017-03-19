#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from PIL import Image, ImageFilter
import subprocess
import time
from selenium import webdriver
from urllib.request import urlretrieve



def test_pillow():
    kitten = Image.open("kitten.png")
    blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
    blurryKitten.save("kitten_blurred.png")
    blurryKitten.show()


def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)

    subprocess.call(["tesseract", newFilePath, "output"])

    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()


def recognize_image_from_web():
    driver = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')
    driver.get('https://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200')
    time.sleep(2)

    driver.find_element_by_id("sitbLogoImg").click()
    imageList = set()

    time.sleep(5)

    while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
        driver.find_element_by_id("sitbReaderRightPageTurner").click()
    #     time.sleep(2)
    #     pages = driver.find_element_by_xpath("//div[@class='pageImage']/div/img")
    #     for page in pages:
    #         image = page.get_attribute("src")
    #         imageList.add(image)
    #
    driver.quit()
    #
    # for image in sorted(imageList):
    #     urlretrieve(image, "page.jpg")
    #     p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     p.wait()
    #     f = open("page.txt", 'r')
    #     print(f.read())


if __name__ == '__main__':
    recognize_image_from_web()