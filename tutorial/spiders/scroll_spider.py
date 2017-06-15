import json
import scrapy


class ScrollSpider(scrapy.Spider):
    ''' Spider that crawls infinitely scrolling web page '''
    name = 'scroll'

    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                'quote': (quote['text']),
                'author': quote['author']['name'],
                'tags': quote['tags'],
            }
        if data['has_next']:
            next_url = self.api_url.format(data['page']+1)
            yield scrapy.Request(next_url, self.parse)
