# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class StockScrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline(object):
	def __init__(self):
		self.file = open('stock.txt', 'a',encoding='utf-8')

	def process_item(self,item,spider):
		line = json.dumps(dict(item)) + '\n'
		#print(line)
		self.file.write(line)
		#self.file.write('\n')
		#self.file.close()
		return item

	def __del__(self):
		self.file.close()