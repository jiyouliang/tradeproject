# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    detail_url = scrapy.Field()  # 详情页地址
    position = scrapy.Field()
    feeback = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    status_value = scrapy.Field()
    type_id = scrapy.Field()
    recruit_num = scrapy.Field()
    date = scrapy.Field()
