# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SuncrawlproItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    num = scrapy.Field()

class Detail_item(scrapy.Item):
    content = scrapy.Field()
    num = scrapy.Field()

