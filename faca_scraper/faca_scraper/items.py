# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FACAScraperItem(scrapy.Item):
    # The source URL
    url_from = scrapy.Field()
    # The destination URL
    url_to = scrapy.Field()
    # agency name
    agency = scrapy.Field()
    # committee name
    name = scrapy.Field()
    # committee url
    committee_url = scrapy.Field()
    # committee status
    status = scrapy.Field()
