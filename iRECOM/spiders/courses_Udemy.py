from scrapy import Spider
from scrapy.selector import Selector
from iRECOM.items import IrecomItem
import scrapy

class StackedSpider(Spider):
    name ="Udemy"
    
    def start_requests(self):
        base_url = "https://www.udemy.com/courses/it-and-software/"
        for page_number in range(1, 626):
            yield scrapy.Request(url="{base_url}{page_number}".format(base_url = base_url, page_number = page_number), callback=self.parse)

    def parse(self, response):
        URL=response.css('').getall()
        allow_domainss=""
        for url in URL:
            next_url= allow_domainss + url
            yield scrapy.Request(url=next_url,callback=self.parse_course_page)
 