import scrapy
import os

class TableSpider(scrapy.Spider):
    ''' Spider that parses HTML table data and extracts quotes '''
    name = 'table'

    start_urls = ['http://quotes.toscrape.com/tableful/']

    def parse(self, response):
        tr = response.xpath('//tr[@style="border-bottom: 0px; "]')
        for row in tr:
            td = row.xpath('./td/text()').extract_first().split('Author:')
            tags = row.xpath('./following::tr[1]/td/a/text()').extract()
            print(tags)
            yield {
                'quote': td[0].strip(),
                'author': td[1].strip(),
                'tags': tags
            }
