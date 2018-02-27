# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class JinanhouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Residential_Brief(scrapy.Item):
    residential_id = Field()
    residential_name = Field()
     # = Field()
    district = Field()
    bizcircle = Field()
    build_year = Field()
    avg_price = Field()
    avg_price_date = Field()
    on_sale_count = Field()


class Residential_Detail(scrapy.Item):
    residential_id = Field()
    residential_name = Field()
    address = Field()
    build_year = Field()
    build_type = Field()
    property_cost = Field()
    property_company = Field()
    avg_price = Field()
    avg_price_date = Field()
    develop_company = Field()
    building_count = Field()
    house_count = Field()
    near_shop = Field()
    lat_lon = Field()
    # on_sale_count = Field()


class around_facilities(Item):
    residential_id = Field()
    residential_name = Field()
    facility_name = Field()
    facility_type1 = Field()
    facility_type2 = Field()
    facility_address = Field()
    facility_distance = Field()


class deal_brief(Item):
    residential_id = Field()
    house_id = Field()
    residential_name = Field()
    title = Field()
    house_info = Field()
    deal_date = Field()
    total_price = Field()
    flood = Field()
    unit_price = Field()
    deal_house_info = Field()
    deal_cycle_info = Field()


class deal_detail(Item):
    house_id = Field()
    deal_price = Field()
    avge_price = Field()
    on_sale_price = Field()
    deal_cycle = Field()
    price_change = Field()
    showings = Field()
    follow = Field()
    page_view = Field()


class house_baseinfo(Item):
    residential_id = Field()
    house_id = Field()
    house_type = Field()
    floor = Field()
    area = Field()
    family_structure = Field()
    inner_area = Field()
    build_type = Field()
    orientation = Field()
    build_year = Field()
    renovation_status = Field()
    build_structure = Field()
    heating_mode = Field()
    elevator_status = Field()
    property_period = Field()
    has_elevator = Field()
    on_sale_date = Field()
    lianjia_id = Field()
    house_purpose = Field()
    house_period = Field()
    ownership = Field()


class ajk_residential_brief_item(Item):
    residential_id = Field()
    residential_name = Field()
    address = Field()
    build_year = Field()
    lat_lon = Field()
    unit_price = Field()
    pct_change_down = Field()
    pct_change_no = Field()
    pct_change_up = Field()

class ajk_residential_baseinfo_item(Item):
    residential_id = Field()
    residential_name = Field()
    avge_price = Field()
    pct_change_down = Field()
    pct_change_level = Field()
    pct_change_up = Field()
    address = Field()
    property_type = Field()
    property_cost = Field()
    area = Field()
    house_count = Field()
    build_year = Field()
    parking_count = Field()
    volumetric_rate = Field()
    green_rate = Field()
    develop_company = Field()
    property_company = Field()
    second_house_count = Field()
    rental_count = Field()


class ftx_residential_brief_item(Item):
    residential_id = Field()
    residential_name = Field()
    build_index = Field()
    build_type = Field()
    address = Field()
    on_sale_count = Field()
    rental_count = Field()
    build_year = Field()
    price = Field()


class ftx_residential_baseinfo_item(Item):
    residential_id = Field()
    residential_name = Field()
    price = Field()
    price_mon_change = Field()
    price_year_change = Field()
    build_year = Field()
    on_sale = Field()
    build_type = Field()
    trade_count = Field()
    house_count = Field()
    build_area = Field()
    ground_area = Field()
    volumetric_rate = Field()
    green_rate = Field()
    address = Field()
    build_count = Field()
    property_company = Field()
    develop_company = Field()
    district = Field()

class ftx_residential_trade_item(Item):
    residential_id = Field()
    residential_name = Field()
    house_type = Field()
    floor = Field()
    orientation = Field()
    area = Field()
    trade_date = Field()
    price = Field()
    unit_price = Field()
