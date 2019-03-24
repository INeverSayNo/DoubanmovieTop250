# -*- coding: utf-8 -*-

#author:anbinjie


import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    pic_url = scrapy.Field()
    inq = scrapy.Field()
    pass
