# -*- coding: utf-8 -*-

__author__ = 'Jerry Lee'

import scrapy
from ..items import IncomeReportItem, BalanceReportItem, CashFlowReportItem
from scrapy.http import Request
import re
import json


class XueQiuCashFlowReportSpider(scrapy.Spider):
    '''
    雪球年报爬虫
    '''
    name = 'xueqiu_cashflow_report'
    #allowed_domains = ['*.xueqiu.com']
    start_urls = ['https://stock.xueqiu.com/']
    download_delay = 5

    def __init__(self, *args, **kwargs):
        super(XueQiuCashFlowReportSpider, self).__init__(*args, **kwargs)

        self.security_code = 'SZ001872'

        self.num_of_page = 0

        #self.start_urls = ['https://stock.xueqiu.com/v5/stock/finance/cn/income.json?symbol=%s&type=Q4&is_detail=true&count=10&timestamp=' % self.security_code]
        self.start_urls = ['https://xueqiu.com']

    def parse_income_report(self, response):
        json_data = json.loads(response.body_as_unicode())
        if json_data['error_code'] == 0:
            data = json_data['data']
            for report in data['list']:
                item = IncomeReportItem()

                for key in report.keys():
                    item[key] = report[key]

                yield item

    def parse_cashflow_report(self, response):
        json_data = json.loads(response.body_as_unicode())
        if json_data['error_code'] == 0:
            data = json_data['data']
            for report in data['list']:
                item = CashFlowReportItem()

                for key in report.keys():
                    item[key] = report[key]

                yield item

    def parse(self, response):
        if response.status == 200:
            url = 'https://stock.xueqiu.com/v5/stock/finance/cn/cash_flow.json?symbol=%s&type=Q4&is_detail=true&count=10&timestamp=' % self.security_code
            yield Request(url, callback=self.parse_cashflow_report, dont_filter=True)


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




