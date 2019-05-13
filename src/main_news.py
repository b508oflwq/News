# -*- coding: utf-8 -*-

import os

from scrapy.crawler import CrawlerProcess

from news.spiders import information

from scrapy.settings import Settings


def main():
    settings = Settings()
    settings_module_path = os.environ.get('SCRAPY_ENV', 'news.settings')
    settings.setmodule(settings_module_path, priority='project')
    process = CrawlerProcess(settings)
    process.crawl(information.NewsSpider)
    process.start()


if __name__ == '__main__':

    main()