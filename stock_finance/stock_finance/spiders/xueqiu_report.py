# -*- coding: utf-8 -*-

__author__ = 'Jerry Lee'

import scrapy
from ..items import XueQiuReportItem
from scrapy.http import Request
import re
import json
from csv import DictReader


class XueQiuReportSpider(scrapy.Spider):
    '''
    雪球年报爬虫
    '''
    name = 'xueqiu_report'
    allowed_domains = ['xueqiu.com']
    start_urls = ['https://stock.xueqiu.com/']
    download_delay = 10

    def __init__(self, *args, **kwargs):
        super(XueQiuReportSpider, self).__init__(*args, **kwargs)

        self.start_urls = ['https://stock.xueqiu.com/']

    def start_requests(self):
        with open('/home/ubuntu/data/instruments.csv') as rows:
            for row in DictReader(rows):
                security_code = row['code']
                prefix = 'SZ' if (security_code[0] == '0' or security_code[0] == '3') else 'SH'
                security_code = prefix + security_code
                url = 'https://xueqiu.com/snowman/S/%s/detail' % security_code
                yield Request(url, callback=self.parse, method="get", meta={"security_code": security_code, "security_name": row['name']})

    def parse_report(self, response):
        item = XueQiuReportItem()
        item['security_code'] = response.meta['security_code'][2:]
        item['security_name'] = response.meta['security_name']
        item['report_type'] = response.meta['report_type']
        item['report_data'] = response.body_as_unicode()

        yield item

    def parse(self, response):
        security_code = response.meta["security_code"]
        security_name = response.meta["security_name"]

        url = 'https://stock.xueqiu.com/v5/stock/finance/cn/balance.json?symbol=%s&type=Q4&is_detail=true&count=10&timestamp=' % security_code
        yield Request(url, callback=self.parse_report, meta={"security_code": security_code, "security_name": security_name, "report_type": 0})

        url = 'https://stock.xueqiu.com/v5/stock/finance/cn/income.json?symbol=%s&type=Q4&is_detail=true&count=10&timestamp=' % security_code
        yield Request(url, callback=self.parse_report, meta={"security_code": security_code, "security_name": security_name, "report_type": 1})

        url = 'https://stock.xueqiu.com/v5/stock/finance/cn/cash_flow.json?symbol=%s&type=Q4&is_detail=true&count=10&timestamp=' % security_code
        yield Request(url, callback=self.parse_report, meta={"security_code": security_code, "security_name": security_name, "report_type": 2})

        url = 'https://stock.xueqiu.com/v5/stock/finance/cn/indicator.json?symbol=%s&type=Q4&is_detail=true&count=10&timestamp=' % security_code
        yield Request(url, callback=self.parse_report, meta={"security_code": security_code, "security_name": security_name, "report_type": 3})



