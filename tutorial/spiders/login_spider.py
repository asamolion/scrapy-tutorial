import scrapy
import json


class FccSpider(scrapy.Spider):
    name = 'login'

    start_urls = ['https://mail.google.com/mail/u/0/#inbox']

    def parse(self, response):
        print(response.xpath('//h1[@class="flat-top wrappable"]/text()').extract_first())
