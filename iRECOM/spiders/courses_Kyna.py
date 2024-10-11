from scrapy import Spider
from scrapy.selector import Selector
from iRECOM.items import IrecomItem
import scrapy

class StackSpider (Spider):
    name = "kyna"
    
    def start_requests(self):
        url = "https://skills.kynaenglish.vn/danh-sach-khoa-hoc/it-va-lap-trinh"
        yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        URL=response.xpath('//div[@class="inner"]/a[@class="view-detail"]/@href').extract()
        allow_domainss="https://skills.kynaenglish.vn"
        for url in URL:
            next_url= allow_domainss + url
            yield scrapy.Request(url=next_url,callback=self.parse_course_page)
    
    def parse_course_page(self,response):     
        yield{
            'url' : response.url,
            'Title' : response.xpath('//div[@class="course-detail--left"]/h1/text()').get(),
            'Duration' : response.xpath('//*[@id="course-detail"]/div[3]/div[2]/div[2]/div/ul/li[2]/p/text()').get(),
            'People Rating' : response.xpath('//div[@class="course-rating-summary"]/span[2]/span[2]/text()').get(),
            'Number Student' : response.xpath('//*[@id="course-detail"]/div[3]/div[2]/div[2]/div/ul/li[1]/p/text()').get()
        }  
    
    