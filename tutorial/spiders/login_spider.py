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
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'aziz', 'password': 'aziz'},
            callback=self.after_login
        )

    def after_login(self, response):
        # The API gives 200 OK as response code even after invalid login, 
        # no choice but to use the following authentication method
        if str.encode("Username") in response.body:
            self.logger.error("Login failed")
            return
        print("Login successful")
        yield response.follow(url='http://restframework.herokuapp.com/snippets/',
                              callback=self.parse_snippets)

    def parse_snippets(self, response):
        div = response.xpath('//div[@class="response-info"]/pre/text()').extract()
        yield json.loads(' '.join(div))
        next_link = response.xpath(
            '//a[@aria-label="Next"]/@href').extract_first()
        yield response.follow(next_link, callback=self.parse_snippets)
        