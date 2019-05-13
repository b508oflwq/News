# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    image_url = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    parapraghs = scrapy.Field()
    file_name = scrapy.Field()
    json_name = scrapy.Field()

