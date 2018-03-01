import scrapy
from JiNanHouse.items import ftx_residential_baseinfo_item, ftx_residential_brief_item, ftx_residential_trade_item
from JiNanHouse.utils import format

class fangtianxiaSpider(scrapy.Spider):
    name = 'fangtianxiaSpider'
    # start_urls = ['http://esf.jn.fang.com/housing/__0_0_0_0_%d_0_0_0/' % i for i in range(1, 2)]
    start_urls = ['http://esf.jn.fang.com/housing/__0_0_0_0_%d_0_0_0/' % i for i in range(1, 101)]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        sel = scrapy.Selector(response=response)
        nodes = sel.xpath('//div[@class="houseList"]/div[@class="list rel"]')
        for node in nodes:
            item = ftx_residential_brief_item()
            eles = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/a[@class="plotTit"]/@href').extract()
            item['residential_id'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/a[@class="plotTit"]/text()').extract()
            item['residential_name'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/span[@class="plotFangType"]/text()').extract()

            eles = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/span[@class="dj"]/li[@class="half"]').extract()
            els2 = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/span[@class="dj"]/li[@class="no2"]').extract()
            item['build_type'] = 5 - len(els2) - 0.5 * len(eles)

            eles = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p[2]/a/text()|./dl[@class="plotListwrap clearfix"]/dd/p[2]/text()').extract()
            item['address'] = "".join([format(e) for e in eles])

            eles = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/ul[@class="sellOrRenthy clearfix"]/li[1]/a/text()').extract()
            item['on_sale_count'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/ul[@class="sellOrRenthy clearfix"]/li[2]/a/text()').extract()
            item['rental_count'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/ul[@class="sellOrRenthy clearfix"]/li[3]/text()').extract()
            item['build_year'] = format(eles[0]) if len(eles) > 0 else ''


            eles = node.xpath('./div[@class="listRiconwrap"]/p[@class="priceAverage"]/span/text()').extract()
            item['price'] = "".join([format(e) for e in eles])

            eles = node.xpath('./div[@class="listRiconwrap"]/p[@class="ratio"]/span/text()').extract()
            item['price_pct_change'] = format(eles[0]) if len(eles) > 0 else ''
            yield item

        for node in nodes:
            eles = node.xpath('./dl[@class="plotListwrap clearfix"]/dd/p/a[@class="plotTit"]/@href').extract()
            url = format(eles[0]) if len(eles) > 0 else ''
            if url != '':
                url_baseinfo = ''
                url_chengjiao = ''
                if url.endswith('esf/'):
                    url_baseinfo = url.replace('esf', 'xiangqing')
                    url_chengjiao = url.replace('esf', 'chengjiao')
                else:
                    url_baseinfo = url + 'xiangqing/'
                    url_chengjiao = url + 'chengjiao/'
                yield scrapy.Request(url_baseinfo, callback=self.residential_baseinfo_parse)
                yield scrapy.Request(url_chengjiao, callback=self.residential_trad_parse)

            else:
                continue

    def  residential_baseinfo_parse(self, response):
        sel = scrapy.Selector(response=response)
        item = ftx_residential_baseinfo_item()

        item['residential_id'] = response.url

        eles = sel.xpath('//div[@class="ceninfo_sq"]/h1/a[@class="tt"]/text()').extract()
        item['residential_name'] = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="box detaiLtop mt20 clearfix"]/dl[1]/dd/span/text()').extract()
        item['price'] = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="box detaiLtop mt20 clearfix"]/dl[2]/dd/span/text()').extract()
        item['price_mon_change'] = format(eles[0]) if len(eles) > 0 else ''

        eles = sel.xpath('//div[@class="box detaiLtop mt20 clearfix"]/dl[@class="last"]/dd/span/text()').extract()
        item['price_year_change'] = format(eles[0]) if len(eles) > 0 else ''

        nodes = sel.xpath('//div[@class="inforwrap clearfix"]/dl[@class=" clearfix mr30"]/dd')
        for node in nodes:
            strong = node.xpath('./strong/text()').extract()[0] if len(node.xpath('./strong/text()').extract()) > 0 else ''
            value = node.xpath('text()').extract()[0] if len(node.xpath('text()').extract())> 0 else ''
            field_map = {'小区地址': 'address', '所属区域': 'district', '物业类别': 'build_type', '建筑年代': 'build_year',
                         '开 发 商': 'develop_company', '建筑类型': 'build_type', '建筑面积': 'build_area',
                         '占地面积': 'build_area', '房屋总数': 'house_count', '楼栋总数': 'build_count',
                         '物业公司': 'property_company', '绿 化 率': 'green_rate', '容 积 率': 'volumetric_rate',
                         '物 业 费': 'property_cost'}
            keys = [key for key in field_map if key in strong]
            for key in keys:
                item[field_map[key]] = value
        yield item

    def residential_trad_parse(self, response):
        sel = scrapy.Selector(response=response)
        nodes = sel.xpath('//div[@class="dealSent sentwrap"]/table/tbody/tr')

        name = sel.xpath('//div[@class="ceninfo_sq"]/h1/a[@class="tt"]/text()').extract()[0]
        for node in nodes:
            item = ftx_residential_trade_item()
            item['residential_id'] = response.url
            item['residential_name'] = name
            eles = node.xpath('./td[@class="firsttd"]/div[@class="hspro"]/p[1]/b/text()').extract()
            item['house_type'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./td[@class="firsttd"]/div[@class="hspro"]/p[2]/text()').extract()
            item['floor'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./td[@class="firsttd"]/div[@class="hspro"]/p[3]/text()').extract()
            item['orientation'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./td[2]/text()').extract()
            item['area'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./td[3]/b/text()').extract()
            item['trade_date'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./td[4]/b/text()').extract()
            item['price'] = format(eles[0]) if len(eles) > 0 else ''

            eles = node.xpath('./td[5]/text()').extract()
            item['unit_price'] = format(eles[0]) if len(eles) > 0 else ''
            yield item

        if response.url.endswith('chengjiao/'):
            page_str = sel.xpath('//div[@class="detailTitle clearfix"]/div[@class="frpageChange  floatr"]/span[@class=" floatl ml10"]/text()').extract()
            page = page_str[0].split('/')[1] if len(page_str) > 0 else 1
            for i in range(1, int(page)):
                url = response.url + '-p1%d-t11/'
                yield scrapy.Request(url % i, callback=self.residential_trad_parse)



















