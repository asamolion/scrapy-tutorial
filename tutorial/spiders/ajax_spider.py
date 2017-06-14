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
                                args={'wait': 3},
                               )
    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]').extract()
        print(quotes)
        pass
