# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    preview = scrapy.Field()
    capacity = scrapy.Field()
    published_time = scrapy.Field()
    details = scrapy.Field()
    download = scrapy.Field()
    click = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()
    data_type = scrapy.Field()
    price = scrapy.Field()
    contact = scrapy.Field()
    lang = scrapy.Field()
    data_category = scrapy.Field()
