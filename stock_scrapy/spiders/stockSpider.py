# -*- coding: utf-8 -*-
import scrapy
from stock_scrapy.items import StockScrapyItem

import json


class StockspiderSpider(scrapy.Spider):
    name = 'stockSpider'
    allowed_domains = ['data.eastmoney.com']
    start_urls = ['http://data.eastmoney.com/DataCenter_V3/gdhs/GetList.ashx?pagesize=50&page=%d' % i for i in range(1,70)]

    def parse(self, response):
        stock_item = StockScrapyItem()

        stock_list = json.loads(response.text)
        stock_data = stock_list['data']

        i = 0

        while i<len(stock_data):

        	if (stock_data[i]['HolderNumChange'] == '') or (stock_data[i]['RangeChangeRate'] == ''):
        		i += 1
        	else:
        		if (float(stock_data[i]['HolderNumChangeRate'])) <= -30.0 and (float(stock_data[i]['HolderNumChangeRate'])) >= -60.0 and (float(stock_data[i]['RangeChangeRate'])) < 0 and stock_data[i]['EndDate'].split('-')[0] == '2018':
        			stock_item['code'] = stock_data[i]['SecurityCode']
        			stock_item['name'] = stock_data[i]['SecurityName']
        			stock_item['numchange'] = float(stock_data[i]['HolderNumChange'])
        			stock_item['numchangeRate'] = float(stock_data[i]['HolderNumChangeRate'])
        			stock_item['endDate'] = stock_data[i]['EndDate']
        			stock_item['previousDate'] = stock_data[i]['PreviousEndDate']
        			i += 1
        			yield stock_item
        		else:
        			i += 1