# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from news.spiders.information import NewsSpider
import scrapy


class ImagePipline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 1 获取图片链接
        for imageLink in item["image_url"]:
            # 2 向图片链接发请求,响应会保存在settings.py中的IMAGES_STORE路径中
            yield scrapy.Request('http://news.hit.edu.cn' + imageLink)


class JsonPipeline(object):
    # def __init__(self):
    #

    def process_item(self, item, spider):
        json_name = item["json_name"]
        self.file = open('news/json/'+json_name+'.json', "wb+")  # 必须二进制写入
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        # 开始写入
        self.exporter.start_exporting()
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 完成写入
        self.exporter.finish_exporting()
        self.file.close()