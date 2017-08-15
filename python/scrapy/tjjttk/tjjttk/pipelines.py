# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RecordItemPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.csv', 'w+')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        return ', '.join(item.values)
