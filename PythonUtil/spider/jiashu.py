# coding=utf-8

__author__ = 'xubinggui'

import scrapy

class JianshuSpider(scrapy.Spider):

    # name of spider
    name = "jianshu"
    # url
    start_urls = ["http://www.jianshu.com/collections/16/notes?order_by=added_at"]

    # callback
    def parse(self, response):
        for item in response.css('.article-list li'):
            # title
            short_url = item.css('h4 a::attr(href)').extract()[0]
            # complete url
            full_url = response.urljoin(short_url)
            print full_url
            yield scrapy.Request(full_url,callback=self.parse_article)

    def parse_article(self, response):
        yield {
            'title':response.css('.preview h1::text').extract()[0],
            'show-content':response.css('.preview .show-content').extract()[0],
            'link':response.url,
        }

