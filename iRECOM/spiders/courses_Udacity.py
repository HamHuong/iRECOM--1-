import scrapy

class StackSpider(scrapy.Spider):
    name = "udacity"

    def start_requests(self):
        base_url = "https://www.udacity.com/catalog/all/any-price/any-school/any-skill/any-difficulty/any-duration/any-type/most-popular/page-"
        for page_number in range(1, 26):
            yield scrapy.Request(url=f"{base_url}{page_number}", callback=self.parse)
        yield scrapy.Request(url=f"{base_url}", callback=self.parse)

    def parse(self, response):
        # Xử lý trang 404
        if response.status == 404:
            self.logger.error(f"404 Not Found: {response.url}")
            return

        # Xử lý trang 500
        if response.status == 500:
            self.logger.error(f"500 Internal Server Error: {response.url}")
            return

        URLs = response.xpath('//div[@class="css-15q7znr"]/a/@href').extract()
        allow_domains = "https://www.udacity.com/course"
        for url in URLs:
            next_url = allow_domains + url
            yield scrapy.Request(url=next_url, callback=self.parse_course_page)

    def parse_course_page(self, response):
        yield {
            'url': response.url,
            'Title': response.xpath('//h1/text()').get(),
            'Duration': response.xpath('//p[contains(text(), "Duration")]/following-sibling::p/text()').get(),
            'People Rating': response.xpath('//p[contains(text(), "People Rating")]/text()').get(),
            # 'Number Student': response.xpath('//span[contains(text(), "Học viên")]/text()').get()
        }
