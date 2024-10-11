# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.selector import Selector
from iRECOM.items import IrecomItem
from scrapy.http import HtmlResponse
import re

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class IrecomPipeline:
    def process_item(self, item, spider):
        # filename = '{luat}.json'.format(luat = item['LawName'].replace("/", "-"))
        self.file = open('data2.json', 'a', encoding='utf-8')
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        print(line)
        self.file.write(line)
        self.file.close()
        return item
