import scrapy
import json
import re
import os


class LoginSpider(scrapy.Spider):
    ''' Login to restframework.herokuapp.com and parse all the snippets
        and the write them to rest.json
    '''
    name = 'login'

    allowed_domains = ['restframework.herokuapp.com']
    start_urls = ['http://restframework.herokuapp.com/api-auth/login/']

    def parse(self, response):
        os.remove('rest.json') 
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'aziz', 'password': 'aziz'},
            callback=self.after_login
        )

    def after_login(self, response):
        if str.encode("Username") in response.body:
            self.logger.error("Login failed")
            return
        print("Login successful")
        yield response.follow(url='http://restframework.herokuapp.com/snippets/',
                              callback=self.parse_snippets)

    def parse_snippets(self, response):
        f = open('rest.json', 'a')
        div = response.xpath('//div[@class="response-info"]').extract_first()
        div = re.sub('<b.*?>(.+?)</b>', '', div)
        div = re.sub('<span.*?>.*|\n*</span>', '', div)
        div = re.sub('<pre.*?>', '', div)
        div = re.sub('</pre>', '', div)
        div = re.sub('<div.*?>', '', div)
        div = re.sub('</div>', '', div)
        div = re.sub('<a.*?>', '', div)
        div = re.sub('</a>', '', div)
        json_data = div
        f.write(json_data)
        next_link = response.xpath(
            '//a[@aria-label="Next"]/@href').extract_first()
        yield response.follow(next_link, callback=self.parse_snippets)
