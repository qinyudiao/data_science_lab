import scrapy

from scrapy.item import Item, Field

class PapercrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()