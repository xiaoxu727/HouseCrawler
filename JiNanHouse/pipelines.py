# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from JiNanHouse.items import Residential_Brief, Residential_Detail, ajk_residential_brief_item, ajk_residential_baseinfo_item, ftx_residential_trade_item, ftx_residential_brief_item, ftx_residential_baseinfo_item
import json
import codecs
from datetime import datetime
import os


def get_file_name(filename, suffix):
    dateStr = datetime.now().strftime('%Y%m%d%H%M%S')
    return dateStr + '_' + filename + '.' + suffix

def remove_file(file):
    if os.path.exists(file.name):
        os.remove(file.name)

class JinanhousePipeline(object):
    def process_item(self, item, spider):
        return item

class ResidentPipeline(object):

    def __init__(self):
        self.residentBriefFile = codecs.open(get_file_name('lj_resident_brief', 'json'), 'w', encoding='utf-8')
        self.residentDetailFile = codecs.open(get_file_name('lj_resident_detail', 'json'), 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name != 'LianjiaSpider':
            self.close_spider()
            remove_file(self.residentBriefFile)
            remove_file(self.residentDetailFile)
            return item
        lines = json.dumps(dict(item), ensure_ascii=False)

        if isinstance(item, Residential_Brief):
            self.residentBriefFile.write(lines)
            self.residentBriefFile.flush()

        elif isinstance(item, Residential_Detail):
            self.residentDetailFile.write(lines)
            self.residentDetailFile.flush()

        return item

    def close_spider(self):

        self.residentBriefFile.close()
        self.residentDetailFile.close()


class AnjukePipline(object):

    def __init__(self):
        self.ajk_residential_brief_file = codecs.open(get_file_name('ajk_resident_brief', 'json'), 'w+', encoding='utf-8')
        self.ajk_residential_baseinfo_file = codecs.open(get_file_name('ajk_resident_baseinfo', 'json'), 'w+', encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name != 'anjukeSpider':
            self.close_spider()

            remove_file(self.ajk_residential_baseinfo_file)
            remove_file(self.ajk_residential_brief_file)
            return item

        lines = json.dumps(dict(item), ensure_ascii=False)
        if isinstance(item, ajk_residential_brief_item):
            self.ajk_residential_brief_file.write(lines)
            self.ajk_residential_brief_file.flush()

        elif isinstance(item, ajk_residential_baseinfo_item):
            self.ajk_residential_baseinfo_file.write(lines)
            self.ajk_residential_baseinfo_file.flush()

        return item

    def close_spider(self):

        self.ajk_residential_brief_file.close()
        self.ajk_residential_baseinfo_file.close()


class FangtianxiaPipline(object):

    def __init__(self):
        self.ftx_residential_brief_file = codecs.open(get_file_name('ftx_resident_brief', 'json'), 'w+', encoding='utf-8')
        self.ftx_residential_baseinfo_file = codecs.open(get_file_name('ftx_resident_baseinfo', 'json'), 'w+', encoding='utf-8')
        self.ftx_residential_trade_file = codecs.open(get_file_name('ftx_resident_trade', 'json'), 'w+', encoding='utf-8')


    def process_item(self, item, spider):
        if spider.name != 'fangtianxiaSpider':
            self.close_spider()
            remove_file(self.ftx_residential_brief_file)
            remove_file(self.ftx_residential_baseinfo_file)
            remove_file(self.ftx_residential_trade_file)
            return item
        lines = json.dumps(dict(item), ensure_ascii=False)
        if isinstance(item, ftx_residential_baseinfo_item):
            self.ftx_residential_baseinfo_file.write(lines)
            self.ftx_residential_baseinfo_file.flush()

        elif isinstance(item, ftx_residential_brief_item):
            self.ftx_residential_brief_file.write(lines)
            self.ftx_residential_brief_file.flush()

        elif isinstance(item, ftx_residential_trade_item):
            self.ftx_residential_trade_file.write(lines)
            self.ftx_residential_trade_file.flush()

        return item

    def close_spider(self):

        self.ftx_residential_baseinfo_file.close()
        self.ftx_residential_brief_file.close()
        self.ftx_residential_trade_file.close()



