# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IrecomItem(scrapy.Item):
    # Faculty = scrapy.Field()
    # Major = scrapy.Field()
    url = scrapy.Field()
    Title = scrapy.Field()
    Duration = scrapy.Field()
   # Major_Subject = scrapy.Field()
    People_Rating = scrapy.Field()
   # Number_Student = scrapy.Field()
    # Supplier = scrapy.Field()
    
    # Additional = scrapy.Field()
