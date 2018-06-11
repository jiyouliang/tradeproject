# -*- coding: utf-8 -*-

import scrapy


class ToutiaoSpider(scrapy.Spider):
    name = "toutiao"
    start_urls = ["https://m.toutiao.com/list/?tag=news_tech&ac=wap&count=20&format=json_raw&as=A135FBB1DC9FFF5"]

    def parse(self, response):
        print("开始解析")
        print("*" * 100)
        print(response.body)

    def start_requests(self):
        print("开始爬虫")
        return super().start_requests()
