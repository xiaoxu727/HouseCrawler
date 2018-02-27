# -*- coding: utf-8 -*-
import scrapy
from JiNanHouse.items import Residential_Brief, Residential_Detail

class LianjiaSpider(scrapy.Spider):
    name = 'LianjiaSpider'
    # allowed_domains = 'jn.lianjia.com'
    # url =
    start_urls = ['https://jn.lianjia.com/xiaoqu/pg%dcro21/' % i for i in range(1, 101)]
    # start_urls = ['https://jn.lianjia.com/xiaoqu/pg1cro21/']
                  # 'https://jn.lianjia.com/xiaoqu/pg2cro21/',
                  # 'https://jn.lianjia.com/xiaoqu/pg3cro21/',
                  # 'https://jn.lianjia.com/xiaoqu/pg4cro21/',
                  # 'https://jn.lianjia.com/xiaoqu/pg5cro21/',
                  # 'https://jn.lianjia.com/xiaoqu/pg6cro21/']
                   # 'https://jn.lianjia.com/xiaoqu/pg7cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg8cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg9cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg10cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg11cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg12cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg13cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg14cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg15cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg16cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg17cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg18cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg19cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg20cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg21cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg22cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg23cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg24cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg25cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg26cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg27cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg28cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg29cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg30cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg31cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg32cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg33cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg34cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg35cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg36cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg37cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg38cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg39cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg40cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg41cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg42cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg43cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg44cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg45cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg46cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg47cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg48cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg49cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg50cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg51cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg52cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg53cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg54cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg55cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg56cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg57cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg58cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg59cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg60cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg61cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg62cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg63cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg64cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg65cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg66cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg67cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg68cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg69cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg70cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg71cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg72cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg73cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg74cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg75cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg76cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg77cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg78cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg79cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg80cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg81cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg82cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg83cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg84cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg85cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg86cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg87cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg88cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg89cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg90cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg91cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg92cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg93cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg94cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg95cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg96cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg97cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg98cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg99cro21/',
                   # 'https://jn.lianjia.com/xiaoqu/pg100cro21/']

    def parse(self, response):
        sel = scrapy.Selector(response=response)

        nodes = sel.xpath('//ul[@class="listContent"]/li')
        for node in nodes:
            item = Residential_Brief()
            eles = node.xpath('./div[@class="info"]/div[@class="title"]/a/@href').extract()
            item['residential_id'] = eles[0] if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="info"]/div[@class="title"]/a/text()').extract()
            item['residential_name'] = eles[0] if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="info"]/div[@class="positionInfo"]/a[@class="district"]/text()').extract()
            item['district'] = eles[0] if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="info"]/div[@class="positionInfo"]/a[@class="bizcircle"]/text()').extract()
            item['bizcircle'] = eles[0] if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="info"]/div[@class="positionInfo"]/text()').extract()
            item['build_year'] = eles[0] if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="xiaoquListItemRight"]/div[@class="xiaoquListItemPrice"]/div[@class="totalPrice"]/span/text()').extract()
            item['avg_price'] = eles[0] if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="xiaoquListItemRight"]/div[@class="xiaoquListItemPrice"]/div[@class="priceDesc"]/text()').extract()
            item['avg_price_date'] = eles[0] if len(eles) > 0 else ''

            eles = node.xpath('./div[@class="xiaoquListItemRight"]/div[@class="xiaoquListItemSellCount"]/a[@class="totalSellCount"]/span/text()').extract()
            item['on_sale_count'] = eles[0] if len(eles) > 0 else ''
            yield item

        for node in nodes:
            eles = node.xpath('./div[@class="info"]/div[@class="title"]/a/@href').extract()
            url = eles[0] if len(eles) > 0 else ''
            if url != '':
                yield scrapy.Request(url, callback=self.resident_detail_parse)
            else:
                continue

    def resident_detail_parse(self, response):
        sel = scrapy.Selector(response=response)
        item = Residential_Detail()
        item['residential_id'] = response.url
        eles = sel.xpath("//div[@class='detailHeader fl']/h1[@class='detailTitle']/text()").extract()
        item['residential_name'] = eles[0] if len(eles) > 0 else ''
        eles = sel.xpath("//div[@class='detailHeader fl']/div[@class='detailDesc']/text()").extract()
        item['address'] = eles[0] if len(eles) > 0 else ''

        eles = sel.xpath("//div[@class='xiaoquOverview']/div[@class='xiaoquDescribe fr']/div[@class='xiaoquInfo']/div[@class='xiaoquInfoItem']/span[@class='xiaoquInfoContent']/text()").extract()
        item['build_year'] = eles[0] if len(eles) > 0 else ''
        item['build_type'] = eles[1] if len(eles) > 1 else ''
        item['property_cost'] = eles[2] if len(eles) > 2 else ''
        item['property_company'] = eles[3] if len(eles) > 3 else ''
        item['develop_company'] = eles[4] if len(eles) > 4 else ''
        item['building_count'] = eles[5] if len(eles) > 5 else ''
        item['house_count'] = eles[6] if len(eles) > 6 else ''
        item['near_shop'] = eles[7] if len(eles) > 7 else ''

        eles = sel.re("resblockPosition.+?',")
        item['lat_lon'] = str.replace(eles[0], 'resblockPosition:', '').replace("'", "") if len(eles) > 0 else ''
        yield item
