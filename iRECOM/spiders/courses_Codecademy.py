from typing import Iterable
from scrapy import Spider
from scrapy.selector import Selector
from iRECOM.items import IrecomItem
import scrapy

class StackSpider(Spider):
    name = "codecademy"
    
    def start_requests(self):
        base_url = "https://www.codecademy.com/catalog"
        for page_number in range(1, 12):
            yield scrapy.Request(url="{base_url}{page_number}".format(base_url = base_url, page_number = page_number), callback=self.parse)


    def parse(self, response):
        URL=response.xpath('//div[@class="gamut-hdtkrl-FlexBox e1tc6bzh0"]/a/@href').extract()
        allow_domainss="https://www.codecademy.com/learn"
        for url in URL:
            next_url= allow_domainss + url
            yield scrapy.Request(url=next_url,callback=self.parse_course_page)
    
    def parse_course_page(self,response):     
        yield{
            'url' : response.url,
            'Title' : response.xpath('//div[@class="gamut-1sjfsmj-Box ebnwbv90"]/h1/text()').get(),
            'Duration' : response.xpath('//ul[@class="gamut-101z6f4-Box ebnwbv90"]/li[2]/div/div[2]/span/text()').get(),
            #'Major Subject' : response.css('a.tag span::text').get(),
            'People Rating' : response.xpath('//div[@class="gamut-1kz499l-FlexBox e1tc6bzh0"]/span/text()').get(),
            'Number Student' : response.xpath('//div[@class="gamut-1jz378k-FlexBox e1tc6bzh0"]/span/strong/text()').get()
            }     
      