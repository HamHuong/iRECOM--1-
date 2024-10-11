from scrapy import Spider
from scrapy.selector import Selector
from iRECOM.items import IrecomItem
import scrapy


class StackSpider(Spider):
    name = "vyy"

    def start_requests(self):
        base_url = "https://unica.vn/tag/cong-nghe-thong-tin?page="
        for page_number in range(0, 6):
            yield scrapy.Request(url="{base_url}{page_number}".format(base_url = base_url, page_number = page_number), callback=self.parse)

    def parse(self, response):
        URL=response.css('a.link-course::attr(href)').getall()
        allow_domainss="https://unica.vn"
        for url in URL:
            next_url= allow_domainss + url
            yield scrapy.Request(url=next_url,callback=self.parse_course_page)
    
    def parse_course_page(self,response):     
        yield{
            'url' : response.url,
            'Title' : response.css('.u-detail-block-title h1 span::text').get(),
            'Duration' : response.css('.block-ulti li  p::text').get(),
            'Major Subject' : response.css('a.tag span::text').get(),
            'People Rating' : response.css('.u-detail-rate span::text').get(),
            'Number Student' : response.xpath("/html/body/main/div[3]/div[1]/div[2]/div[4]/span/text() [contains (.,'Học viên')]").get()
        }     
      
        