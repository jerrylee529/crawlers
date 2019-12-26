# -*- coding: utf-8 -*-

__author__ = 'Jerry Lee'

import scrapy
from ..items import WDZJItem
from scrapy.http import Request
import re


class WDZJSpider(scrapy.Spider):
    name = 'wdzj'
    allowed_domains = ['www.wdzj.com']
    start_urls = ['https://www.wdzj.com/']
    download_delay = 5

    def __init__(self, *args, **kwargs):
        super(WDZJSpider, self).__init__(*args, **kwargs)

        self.global_page_no = 1

        self.num_of_page = 0

        self.start_urls = ['https://www.wdzj.com/dangan/search?filter=e1&sort=6&currentPage=%d' % self.global_page_no]

    def parse(self, response):
        if response.text.find(u'src="/wdzj/images/front/archive/noresult.png" alt="暂无结果"') >= 0:
            return

        if self.num_of_page == 0:
            num_of_page_text = response.xpath('//div[@class="pageList"]/span/text()').extract()[0]

            print num_of_page_text

            texts = re.findall(r'/(\d+)', num_of_page_text, re.S|re.M)

            self.num_of_page = int(texts[0])

        elements = response.xpath('//div[@id="showTable"]/ul/li')

        for i in range(1, len(elements)+1):
            title_tag = '//div[@id="showTable"]/ul/li[%d]/div[1]/h2/a/text()' % i
            city_tag = '//div[@id="showTable"]/ul/li[%d]/div[2]/a/div[3]/text()' % i
            detail_url_tag = '//div[@id="showTable"]/ul/li[%d]/div[2]/div/a[2]/@href' % i
            title = response.xpath(title_tag).extract()[0]
            city = response.xpath(city_tag).extract()[0]
            detail_url = response.xpath(detail_url_tag).extract()[0]

            pos = city.find(u'：')

            if pos >= 0:
                city = city[pos+1:].strip()

            item = WDZJItem()
            item['company_name'] = title
            item['register_city'] = city

            #yield item

            yield Request("https://www.wdzj.com" + detail_url, callback=self.parse_item, dont_filter=True, meta={"item": item})

        self.global_page_no += 1
        if self.global_page_no <= self.num_of_page:
            url = 'https://www.wdzj.com/dangan/search?filter=e1&sort=6&currentPage=%d' % self.global_page_no
            print url
            yield Request(url, callback=self.parse, dont_filter=True)

    def _convert_number(self, value):
        try:
            result = float(value)
        except Exception as e:
            print(str(e))
            result = 0.0

        return result

    # 解析公司详情
    def parse_item(self, response):
        '''
        income_rate = response.xpath('/html/body/div[7]/div[1]/div[2]/div[2]/div/div[1]/div[3]//div[contains(string(), u"参考收益")]').extract()[0]
        loan_period = response.xpath('/html/body/div[7]/div[1]/div[2]/div[2]/div/div[1]/div[3]//div[contains(string(), u"投资期限")').extract()[0]
        amount = response.xpath('/html/body/div[7]/div[1]/div[2]/div[2]/div/div[1]/div[3]//div[contains(string(), u"昨日成交量")').extract()[0]
        collected_balance = response.xpath('/html/body/div[7]/div[1]/div[2]/div[2]/div/div[1]/div[3]//div[contains(string(), u"昨日待还余额")').extract()[0]
        '''


        income_rate = re.search(r'<div class="box lbor">[\s\S]*<b class="tab_common_data">(.*?)</b>[\s\S]*<div>参考收益</div>', response.body, re.M|re.I).group(1)
        loan_period = re.search(r'<div class="box lbor">[\s\S]*<b class="tab_common_data">(.*?)</b>[\s\S]*<div>投资期限</div>', response.body, re.M|re.I).group(1)
        amount = re.search(r'<div class="box lbor">[\s\S]*<b class="tab_common_data">(.*?)</b>[\s\S]*<div>昨日成交量</div>', response.body, re.M|re.I).group(1)
        collected_balance = re.search(r'<div class="box lbor">[\s\S]*<b class="tab_common_data">(.*?)</b>[\s\S]*<div>昨日待还余额</div>', response.body, re.M|re.I).group(1)


        item = response.meta['item']
        item['amount'] = self._convert_number(amount)
        item['collected_balance'] = self._convert_number(collected_balance)
        item['income_rate'] = self._convert_number(income_rate)
        item['loan_period'] = self._convert_number(loan_period)

        yield item


