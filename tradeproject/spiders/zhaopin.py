# -*- coding: utf-8 -*-

import scrapy
import datetime
import time
import random
from tradeproject.items import ZhaopinItem


class ZhaopinSpider(scrapy.Spider):
    name = "zhaopin"
    allowed_domains = ["zhaopin.com"]
    start_urls = ["https://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&sm=0&p=1",
                  "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&sm=0&p=2",
                  "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&sm=0&p=3"]

    def parse(self, response):
        # ret = response.body
        # 解析
        # table_list = response.xpath("//table[@class='newlist']")
        # 招聘岗位数
        recruit_num = response.xpath("//span[@class='search_yx_tj']/em/text()").extract()[0] if len(
            response.xpath("//span[@class='search_yx_tj']/em/text()").extract()) > 0 else 0
        table_list = response.xpath("//table[@class='newlist']")
        print("*" * 100)
        print("招聘个数", recruit_num)

        items = []
        for table in table_list:
            # 标题
            if table_list.index(table) == 0:
                print("**********************************表头**********************************")
                position_title = table.xpath(".//th[@class='zwmc']/span/text()").extract()[0]
                feeback_title = table.xpath(".//th[2]/text()").extract()[0]
                company_title = table.xpath(".//th[@class='gsmc']/text()").extract()[0]
                salary_title = table.xpath(".//th[@class='zwyx']/text()").extract()[0]
                address_title = table.xpath(".//th[@class='gzdd']/text()").extract()[0]
                data_title = table.xpath(".//th[@class='gxsj']/text()").extract()[0]
                print(position_title, company_title, feeback_title, salary_title, address_title, data_title)
            else:
                item = ZhaopinItem()
                # 职位
                position = table.xpath(".//td[@class='zwmc']/div/a/text()").extract()[0].replace(u'\xa0', u'') if len(
                    table.xpath(".//td[@class='zwmc']/div/a/text()").extract()) > 0 else "None"
                # 反馈率
                feeback = table.xpath(".//td[@class='fk_lv']/span/text()").extract()[0] if len(
                    table.xpath(".//td[@class='fk_lv']/span/text()").extract()) > 0 else "None"
                # 公司名称
                company = table.xpath(".//td[@class='gsmc']/a/text()").extract()[0].replace(u'\xa0', u'') if len(
                    table.xpath(".//td[@class='gsmc']/a/text()").extract()) > 0 else "None"
                salary = table.xpath(".//td[@class='zwyx']/text()").extract()[0] if len(
                    table.xpath(".//td[@class='zwyx']/text()").extract()) > 0 else "None"
                status_value = table.xpath(".//td[@class='gxsj']/span/text()").extract()[0] if len(
                    table.xpath(".//td[@class='gxsj']/span/text()").extract()) > 0 else "None"
                print(table_list.index(table), position, feeback, company, salary, status_value)

                now = datetime.datetime.now()

                item["position"] = position
                item["feeback"] = feeback
                item["company"] = company
                item["salary"] = salary
                item["status_value"] = status_value
                item["date"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                items.append(item)
                yield item

        # print("长度", len(items))
        # yield items
