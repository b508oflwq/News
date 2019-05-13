# -*- coding: utf-8 -*-

import datetime
import json
import scrapy
from collections import OrderedDict
from news.items import NewsItem
from scrapy.exporters import JsonItemExporter


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.hit.edu.cn']

    start_urls = []

    for num in range(1, 267):
        url = 'http://news.hit.edu.cn'
        url_all = url + '/xxyw/' + 'list' + str(num) + '.htm'
        start_urls.append(url_all)

    def parse(self, response):
        global name
        name = str(response.url).split("/")[-1]
        dic = {}
        trs = response.xpath("//*[@id='wp_news_w7']/ul/li/div[1]/span/a")
        for tr in trs:
            href = tr.xpath("./@href").extract_first()
            title = tr.xpath('./text()').extract_first()
            dic["url"] = self.url + href
            dic["title"] = title
            dic["name"] = name
            yield scrapy.Request(url=self.url + href, meta=dic, callback=self.get_data)

    def name(self):
        return name

    def get_data(self, response):
        file_name = []
        item = NewsItem()
        dic = response.meta
        parapraghs = response.xpath('//*[@id="container"]/div/div[1]/div[2]/div/div/div/p[1]/text()').extract_first()
        file_names = response.xpath('//*[@id="container"]/div/div[1]/div[2]/div/div/div/p/img/@sudyfile-attr').extract()
        img_links = response.xpath('//*[@id="container"]/div/div[1]/div[2]/div/div/div/p/img/@original-src').extract()
        for file in file_names:
            filename = file.split(":")[1].split('.')[0].replace("'", "")
            if filename.isdigit():
                continue
            file_name.append(filename)
        item["url"] = dic["url"]
        item["title"] = dic["title"]
        item["parapraghs"] = parapraghs
        item["file_name"] = file_name
        item["json_name"] = dic["name"]

        # 存入json
        # exporter = JsonItemExporter(j, encoding="utf-8", ensure_ascii=False)
        # exporter.start_exporting()
        # exporter.export_item(data)
        # exporter.finish_exporting()

        # 得到图片路径，转入pipelines.py
        item["image_url"] = img_links
        yield item
