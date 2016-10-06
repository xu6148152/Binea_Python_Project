# coding=utf-8

__author__ = 'xubinggui'

import scrapy

class MediumSpider(scrapy.Spider):

    """docstring for MediumSpider"""

    name = "mediumspider"

    start_urls = ["https://medium.com/tag/android"]

    def parse(self, response):
        for postitem in response.css('.postItem'):
            url = postitem.css('article a::attr(href)').extract()[0]

            # get title
            if len( postitem.css('article h2::text').extract() ) != 0 :
                title = postitem.css('article h2::text').extract()[0]
            elif len( postitem.css('article h3::text').extract() ) != 0 :
                title = postitem.css('article h3::text').extract()[0]
            elif len( postitem.css('article h4::text').extract()) != 0 :
                title = postitem.css('article h4::text').extract()[0]
            else:
                 title = "Error get title"


            # get subtitle
            if len( postitem.css('.section-inner h4::text').extract()) != 0 :
                subtitle = postitem.css('.section-inner h4::text').extract()[0]
            elif len( postitem.css('.section-inner p::text').extract()) != 0 :
                subtitle = postitem.css('.section-inner p::text').extract()[0]
            else:
                subtitle = "No subtitle"

            yield {
                "title":title,
                "subtitle":subtitle,
                "url":url,
            }