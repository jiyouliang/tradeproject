# encoding=utf-8
import json
import time

import pymysql
import pymysql.cursors
import requests
from twisted.enterprise import adbapi


class ToutiaoSpidering():

    def __init__(self):
        timestamp = int(time.time())
        self.url = "https://m.toutiao.com/list/?tag=news_tech&ac=wap&count=20&format=json_raw&as=A1B58B21ADB16EA&cp=5B1D21A60E1A8E1&min_behot_time=1528625870&_signature=NsWcrQAAbd6c6twtMmehZjbFnL&i=%s" % timestamp
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }
        print(self.url)

    def request(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content.decode("utf-8")

    def insert(self, data):
        conn = pymysql.connect(host="47.106.182.74", user="root", passwd="09103208", db="toutiao")
        strftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print("时间=", strftime, type(strftime))
        cur = conn.cursor()  # 创建游标
        # 操作数据库,插入数据
        reCount = cur.execute('insert into news_tech(date, _json) values(%s,%s)',
                              (strftime, data))

        conn.commit()  # 提交数据到数据库
        cur.close()
        conn.close()

    def run(self):
        response = self.request()
        self.insert(response)
        # self.parse(response)


if __name__ == '__main__':
    toutiao = ToutiaoSpidering()
    toutiao.run()
