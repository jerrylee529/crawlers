# -*- coding: utf-8 -*-

__author__ = 'Jerry Lee'

import scrapy
from ..items import IncomeReportItem, BalanceReportItem, CashFlowReportItem
from scrapy.http import Request
import re
import json
from csv import DictReader


class XueQiuIncomeReportSpider(scrapy.Spider):
    '''
    雪球年报爬虫
    '''
    name = 'xueqiu_income_report'
    #allowed_domains = ['*.xueqiu.com']
    start_urls = ['https://xueqiu.com/']
    download_delay = 5

    def __init__(self, *args, **kwargs):
        super(XueQiuIncomeReportSpider, self).__init__(*args, **kwargs)

        #self.start_urls = ['https://stock.xueqiu.com/v5/stock/finance/cn/income.json?symbol=%s&type=Q4&is_detail=true&count=10&timestamp=' % self.security_code]
        self.start_urls = ['https://xueqiu.com']

    def start_requests(self):

        with open('E:\\workspace\\TianChengSystem\\code\\07_QuantitativeDataPlatform_QDP\\scrapy\\spider_men\\instruments.csv') as rows:
            for row in DictReader(rows):
                security_code = row['code']
                prefix = 'SZ' if security_code[0] == '0' else 'SH'
                security_code = prefix + security_code
                #url = 'https://stock.xueqiu.com/v5/stock/finance/cn/income.json?symbol=%s&type=Q4&is_detail=true&count=10&timestamp=' % security_code
                url = 'https://xueqiu.com/snowman/S/%s/detail' % security_code
                yield Request(url, callback=self.parse, method="get", meta={"security_code": security_code, "security_name": row['name']})

                break

    def parse_income_report(self, response):
        json_data = json.loads(response.body_as_unicode())
        if json_data['error_code'] == 0:
            data = json_data['data']
            for report in data['list']:
                item = IncomeReportItem()
                '''
                for key in report.keys():
                    if key in item.fields:
                        item[key] = report[key]
                '''
                item['security_code'] = response.meta['security_code'][2:]
                item['security_name'] = response.meta['security_name']
                item['report_date'] = report['report_date']
                item['report_name'] = report['report_name']
                item[''] = report['']
                item[''] = report['']
                item[''] = report['']
                item[''] = report['']
                item[''] = report['']
                item[''] = report['']
                item[''] = report['']

                yield item

    def parse(self, response):
        security_code = response.meta["security_code"]
        security_name = response.meta["security_name"]
        url = 'https://stock.xueqiu.com/v5/stock/finance/cn/income.json?symbol=%s&type=Q4&is_detail=true&count=10&timestamp=' % security_code
        print url
        yield Request(url, callback=self.parse_income_report, meta={"security_code": security_code, "security_name": security_name})

        '''
        self.global_page_no += 1
        if self.global_page_no <= self.num_of_page:
            url = 'https://www.wdzj.com/dangan/search?filter=e1&sort=6&currentPage=%d' % self.global_page_no
            print url
            yield Request(url, callback=self.parse, dont_filter=True)
        '''
    def _convert_number(self, value):
        try:
            result = float(value)
        except Exception as e:
            print(str(e))
            result = 0.0

        return result




