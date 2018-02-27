# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from JiNanHouse.items import Residential_Brief, Residential_Detail, ajk_residential_brief_item, ajk_residential_baseinfo_item
import json
import codecs

class JinanhousePipeline(object):
    def process_item(self, item, spider):
        return item

class ResidentPipeline(object):
    def __init__(self):
        self.residentBriefFile = codecs.open('residentBrief.json', 'w', encoding='utf-8')
        self.residentDetailFile = codecs.open('residentDetail.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False)

        if isinstance(item, Residential_Brief):
            self.residentBriefFile.write(lines)
        elif isinstance(item, Residential_Detail):
            self.residentDetailFile.write(lines)
        return item

    def close_spider(self):
        self.residentBriefFile.close()
        self.residentDetailFile.close()


class AnjukePipline(object):
    def __init__(self):
        self.ajk_residential_brief_file = codecs.open('ajk_resident_brief.json', 'w', encoding='utf-8')
        self.ajk_residential_baseinfo_file = codecs.open('ajk_resident_baseinfo.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):

        lines = json.dumps(dict(item), ensure_ascii=False)
        if isinstance(item, ajk_residential_brief_item):
            self.ajk_residential_brief_file.write(lines)
        elif isinstance(item, ajk_residential_baseinfo_item):
            self.ajk_residential_baseinfo_file.write(lines)
        return item

    def close_spider(self):
        self.ajk_residential_brief_file.close()
        self.ajk_residential_baseinfo_file.close()
