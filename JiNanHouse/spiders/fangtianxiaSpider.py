import scrapy
from JiNanHouse.items import ftx_residential_baseinfo_item, ftx_residential_brief_item, ftx_residential_trade_item

class fangtianxiaSpider(scrapy.Spider):
    name = 'fangtianxiaSpider'
    start_urls = ['http://esf.jn.fang.com/housing/__0_0_0_0_%d_0_0_0/' % i for i in range(1, 101)]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        sel = scrapy.Selector(response=response)
        nodes = sel.xpath('//div[@class="houseList"]/div[@class="list rel"]')
        for node in nodes:
            item = ftx_residential_brief_item()

            els = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/a[@class="plotTit"]/@href').extract()
            item['residential_id'] = els[0] if len(els) > 0 else ''

            els = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/a[@class="plotTit"]/text()').extract()
            item['residential_name'] = els[0] if len(els) > 0 else ''

            els = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/span[@class="plotFangType"]/text()').extract()

            els = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/span[@class="dj"]/li[@class="half"]').extract()
            els2 = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/span[@class="dj"]/li[@class="no2"]').extract()
            item['build_type'] = 5 - len(els2) - 0.5 * len(els)

            els = node.xpath('./dl[@class="plotListwrap clearfix"]/a/text()').extract()
            item['address'] = ''.join(els)

            els = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/ul[@class="sellOrRenthy clearfix"]/li[1]/a/text()').extract()
            item['on_sale_count'] = els[0] if len(els) > 0 else ''

            els = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/ul[@class="sellOrRenthy clearfix"]/li[2]/a/text()').extract()
            item['rental_count'] = els[0] if len(els) > 0 else ''

            els = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/ul[@class="sellOrRenthy clearfix"]/li[3]/text()').extract()
            item['build_year'] = els[0] if len(els) > 0 else ''


            els = node.xpath('./dl[@class="listRiconwrap"]/div[@class="listRiconwrap"]/p[@class="priceAverage"]/span/text()').extract()
            item['price'] =  "".join(els)

            els = node.xpath('./dl[@class="listRiconwrap"]/div[@class="listRiconwrap"]/p[@class="ratio"]/span/text()').extract()
            item['build_year'] = els[0] if len(els) > 0 else ''
            yield item

            for node in nodes:
                els = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/a[@class="plotTit"]/@href').extract()
                url = els[0] if len(els) > 0 else ''
                if url != '':
                    if url.endswith('esf/'):
                        url = url.replace('esf', 'xiangqing')
                    else:
                        url += 'xiangqing/'
                    yield scrapy.Request(url, callback=self.residential_baseinfo_parse)
                else:
                    continue

    def  residential_baseinfo_parse(self, response):
        sel = scrapy.Selector(response=response)
        item = ftx_residential_baseinfo_item()

        item['residential_id'] = response.url

        els = sel.xpath('//div[@class="ceninfo_sq"]/h1/a[@class="tt"]/text()').extract()
        item['residential_name'] = els[0] if len(els) > 0 else ''

        els = sel.xpath('//div[@class="box detaiLtop mt20 clearfix"]/dl[1]/dd/span/text()').extract()
        item['price'] = els[0] if len(els) > 0 else ''

        els = sel.xpath('//div[@class="box detaiLtop mt20 clearfix"]/dl[2]/dd/span/text()').extract()
        item['price_mon_change'] = els[0] if len(els) > 0 else ''

        els = sel.xpath('//div[@class="box detaiLtop mt20 clearfix"]/dl[@class="last"]/dd/span/text()').extract()
        item['price_year_change'] = els[0] if len(els) > 0 else ''

        els = sel.xpath('//div[@class="inforwrap clearfix"]/dl[@class="clearfix mr30"]/dd/text()').extract()
        item['address'] = els[0] if len(els) > 0 else ''
        item['district'] = els[1] if len(els) > 1 else ''
        item['build_type'] = els[5] if len(els) > 5 else ''
        item['build_year'] = els[6] if len(els) > 6 else ''
        item['develop_company'] = els[7] if len(els) > 7 else ''
        item['build_type'] = els[8] if len(els) > 8 else ''
        item['build_area'] = els[9] if len(els) > 9 else ''
        item['ground_area'] = els[10] if len(els) > 10 else ''
        item['house_count'] = els[11] if len(els) > 11 else ''
        item['build_count'] = els[12] if len(els) > 12 else ''
        item['property_company'] = els[13] if len(els) > 13 else ''
        item['green_rate'] = els[14] if len(els) > 14 else ''
        item['volumetric_rate'] = els[15] if len(els) > 15 else ''
        yield item













