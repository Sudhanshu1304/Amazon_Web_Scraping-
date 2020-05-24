# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    #author=scrapy.Field()
    price=scrapy.Field()
    no_of_reviews=scrapy.Field()
    stars=scrapy.Field()