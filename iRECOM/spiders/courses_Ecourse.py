from scrapy import Spider
from scrapy.selector import Selector
from iRECOM.items import IrecomItem
import scrapy


class StackSpider(Spider):
    name = "vy"

    def start_requests(self):
        base_url = "https://www.ecourses.vn/course-subject/cong-nghe-thong-tin/page/"
        for page_number in range(0, 22):
            yield scrapy.Request(url="{base_url}{page_number}".format(base_url = base_url, page_number = page_number), callback=self.parse)

    def parse(self, response):
        courses = Selector(response).xpath('//div[@class="wp-block-toolset-blocks-container tb-container container-fluid"]')
        for course in courses:

            courseFirstColumn = course.xpath('./descendant::div[@class="wp-block-toolset-blocks-grid-column tb-grid-column tb-grid-align-top"][1]')
            supplier = courseFirstColumn.xpath('./descendant::div[@class="tb-fields-and-text"]/p[1]/a/text()').getall()

            courseSecondColumn = course.xpath('./descendant::div[@class="wp-block-toolset-blocks-grid-column tb-grid-column tb-grid-align-top"][2]')

            facultyAndMajorBlock = courseSecondColumn.xpath('./descendant::div[@class="tb-fields-and-text"][1]')
            faculty = facultyAndMajorBlock.xpath('./descendant::a[1]/text()').get()
            major = facultyAndMajorBlock.xpath('./descendant::a[2]/text()').get()
            title = courseSecondColumn.xpath('./h3[@class="tb-heading"]/a/text()').get()

            additionalInfoBlock = courseSecondColumn.xpath('./descendant::div[@class="tb-fields-and-text"][2]')
            additionalInformation = additionalInfoBlock.xpath('normalize-space(string(./p))').get()


            print("Faculty: {}".format(faculty))
            print("Major: {}".format(major))
            print("Title: {}".format(title))
            print("Supplier: {}".format(supplier))
            print("Additional Information: {}".format(additionalInformation))


            item = IrecomItem()
            item['Faculty'] = faculty
            item['Major'] = major
            item['Title'] = title
            item['Supplier'] = supplier
            yield item  

        

 