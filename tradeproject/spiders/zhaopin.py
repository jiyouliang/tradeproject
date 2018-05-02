# -*- coding: utf-8 -*-

import scrapy


class ZhaopinSpider(scrapy.Spider):
    name = "zhaopin"
    allowed_domains = ["zhaopin.com"]
    start_urls = ["https://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=python&sm=0&p=1"]

    def parse(self, response):
        # ret = response.body
        # 解析
        # table_list = response.xpath("//table[@class='newlist']")
        table_list = response.xpath("//table[@class='newlist']")
        print("*" * 100)

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
                # 职位
                position = table.xpath(".//td[@class='zwmc']/div/a/text()").extract()[0].replace(u'\xa0', u'') if len(
                    table.xpath(".//td[@class='zwmc']/div/a/text()").extract()) > 0 else ""
                # 反馈率
                feeback = table.xpath(".//td[@class='fk_lv']/span/text()").extract()[0] if len(
                    table.xpath(".//td[@class='fk_lv']/span/text()").extract()) > 0 else ""
                # 公司名称
                company = table.xpath(".//td[@class='gsmc']/a/text()").extract()[0].replace(u'\xa0', u'') if len(
                    table.xpath(".//td[@class='gsmc']/a/text()").extract()) > 0 else ""
                salary = table.xpath(".//td[@class='zwyx']/text()").extract()[0] if len(
                    table.xpath(".//td[@class='zwyx']/text()").extract()) > 0 else ""
                status_value = table.xpath(".//td[@class='gxsj']/span/text()").extract()[0] if len(
                    table.xpath(".//td[@class='gxsj']/span/text()").extract()) > 0 else ""
                print(table_list.index(table), position, feeback, company, salary, status_value)
