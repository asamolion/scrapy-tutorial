import scrapy
import json


class FccSpider(scrapy.Spider):
    name = 'fcc'

    start_urls = ['https://www.freecodecamp.com/map']

    def parse(self, response):
        f = open('fcc.json', 'w')
        for h in response.xpath('//h3/a'):
            data = {
                'heading': "",
                'challenges': []
            }
            data['heading'] = h.xpath('./text()').extract_first()
            for challenge in h.xpath('./following::div[1]/p/a/span[1]/text()').extract():
                data['challenges'].append(challenge)

            json.dump(data, f)
        f.close()
