# -*- coding: utf-8 -*-
import scrapy

class Jianshu2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quote = scrapy.Field()
    likeNum = scrapy.Field()
