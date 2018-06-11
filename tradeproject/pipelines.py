# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import sys
from scrapy.conf import settings
import threading
import pymysql
import time
import datetime
from twisted.enterprise import adbapi
from twisted.internet import reactor


class ZhaopinPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("pymysql", host=settings["MYSQL_HOST"], db=settings["MYSQL_DATABASE"],
                                            user=settings["MYSQL_USER"], password=settings["MYSQL_PWD"],
                                            charset="utf8",
                                            cursorclass=pymysql.cursors.DictCursor, use_unicode=True)

    def process_item(self, item, spider):
        table = settings["MYSQL_TABLE_ZHAOPIN"]
        sql = """insert into zhilian(position, feeback, company, salary, date) values(%s, %s, %s, %s, %s)"""
        params = (item["position"], item["feeback"], item["company"], item["salary"], item["date"])
        try:
            query = self.dbpool.runInteraction(self.insert, sql, params)
            query.addCallbacks(self.handle_error)
        except Exception as e:
            print("-" * 100)
            print("异常信息")
            print(e)

        # reactor.callLater(0, reactor.stop)
        # reactor.run()
        return item

    def insert(self, cursor, sql, params):
        """插入数据"""
        cursor.execute(sql, params)

    def handle_error(*args, **kwargs):
        print("*" * 100)
        print("错误")
        print(args)
        print(kwargs)
        print("*" * 100)
