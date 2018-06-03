# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    name = scrapy.Field()
    numchange = scrapy.Field()
    numchangeRate = scrapy.Field()
    rangechangeRate = scrapy.Field()
    endDate = scrapy.Field()
    previousDate = scrapy.Field()
