import scrapy
from scrapy_splash import SplashRequest


class AjaxSpider(scrapy.Spider):
    ''' Spider that extracts AJAXed content 
        i.e. dynamically generated content
    '''

    name = 'ajax'

    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        '''
        WILL NEED SPLASH HEADLESS BROWSER FOR THIS TO WORK!
        '''
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 1},
                               )
    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                'quote': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('./span/small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('./div[@class="tags"]/a/text()').extract()
            }
