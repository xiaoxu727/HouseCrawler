# -*- coding: utf-8 -*-
import scrapy
from JiNanHouse.items import ajk_residential_baseinfo_item, ajk_residential_brief_item
from JiNanHouse.utils import format

class AnjukeSpider(scrapy.Spider):
    name = 'anjukeSpider'
    start_urls = ['https://jinan.anjuke.com/community/o6-p%d/' % i for i in range(1, 51) ]
    headers = {
        ':authority':'jinan.anjuke.com',
        ':method':':GET',
        ':path': '/community/view/1027697',
        ':scheme': 'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept - encoding': 'gzip, deflate, sdch, br',
        'accept - language': 'zh - CN, zh;q = 0.8',
        'cache - control': 'max - age = 0',
        'upgrade - insecure - requests': 1,

        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)

        # yield scrapy.Request(self.start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        sel = scrapy.Selector(response=response)
        nodes = sel.xpath('//div[@class="list-content"]/div[@_soj="xqlb"]')
        for node in nodes:
            item = ajk_residential_brief_item()
            eles = node.xpath('./div[@class="li-info"]/h3/a/@href').extract()
            item['residential_id'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="li-info"]/h3/a/text()').extract()
            item['residential_name'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="li-info"]/address/text()').extract()
            item['address'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="li-info"]/p[@class="date"]/text()').extract()
            item['build_year'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="li-info"]/p[@class="bot-tag"]/a/@href').extract()
            item['lat_lon'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="li-side"]/p/strong/text()').extract()
            item['unit_price'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="li-side"]/p[@class="price-txt price-down"]/text()').extract()
            item['pct_change_down'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="li-side"]/p[@class="price-txt price-no"]/text()').extract()
            item['pct_change_no'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="li-side"]/p[@class="price-txt"]/text()').extract()
            item['pct_change_up'] = format(eles[0]) if len(eles) > 0 else ''
            yield item

        for node in nodes:
            item = ajk_residential_brief_item()
            eles = node.xpath('./div[@class="li-info"]/h3/a/@href').extract()
            url = format(eles[0]) if len(eles) > 0 else ''
            if url != '':
                yield scrapy.Request(url, callback=self.baseinfo_parse, headers=self.headers)
            else:
                continue


    def baseinfo_parse(self, response):
        item = ajk_residential_baseinfo_item()
        sel = scrapy.Selector(response=response)

        item['residential_id'] = response.url

        eles = sel.xpath('//div[@class="comm-title"]/h1/text()').extract()
        item['residential_name'] = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="comm-title"]/h1/span[@class="sub-hd"]/text()').extract()
        item['address'] = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="price"]/span[@class="average"]/text()|//div[@class="price"]/span[@class="average no-data"]/text()').extract()
        item['avge_price'] = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="price"]/span[@class="status up"]/text()').extract()
        item['pct_change_up'] = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="price"]/span[@class="status level"]/text()').extract()
        item['pct_change_level'] = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="price"]/span[@class="status down"]/text()').extract()
        item['pct_change_down'] = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="basic-infos-box"]/dl[@class="basic-parms-mod"]/dd/text()').extract()
        field_map = {'物业类型': 'property_type', '物业费': 'property_cost', '总建面积': 'area', '总户数': 'house_count',
                     '建造年代': 'build_year', '停车位': 'parking_count', '容  积  率': 'volumetric_rate', '绿化率': 'green_rate',
                     '开  发  商': 'develop_company', '物业公司': 'property_company'}
        item['property_type'] = format(eles[0]) if len(eles) > 0 else ''
        item['property_cost'] = format(eles[1]) if len(eles) > 1 else ''
        item['area'] = format(eles[2]) if len(eles) > 2 else ''
        item['house_count'] = format(eles[3]) if len(eles) > 3 else ''
        item['build_year'] = format(eles[4]) if len(eles) > 4 else ''
        item['parking_count'] = format(eles[5]) if len(eles) > 5 else ''
        item['volumetric_rate'] = format(eles[6]) if len(eles) > 6 else ''
        item['green_rate'] = format(eles[7]) if len(eles) > 7 else ''
        item['develop_company'] = format(eles[8]) if len(eles) > 8 else ''
        item['property_company'] = format(eles[9]) if len(eles) > 9 else ''

        eles = sel.xpath('//div[@class="basic-infos-box"]/div[@class="houses-sets-mod j-house-num"]/a[@class="num ershou-num"]/text()').extract()
        second_house_count = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="basic-infos-box"]/div[@class="houses-sets-mod j-house-num"]/a[@data-soj="baseinfozu"]/text()').extract()
        rental_count = format(eles[0]) if len(eles) > 0 else ''
        yield item












