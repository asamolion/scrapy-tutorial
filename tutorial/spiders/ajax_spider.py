import scrapy


class AjaxSpider(scrapy.Spider):
    ''' Spider that extracts AJAXed content 
        i.e. dynamically generated content
    '''
    name = 'ajax'

    start_urls = ['http://quotes.toscrape.com/js/']

    def parse(self, response):
        pass
