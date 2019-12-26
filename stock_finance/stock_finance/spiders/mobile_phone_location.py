# -*- coding: utf-8 -*-

import scrapy

from ..items import SpiderMenItem


class MobilePhoneLocationSpider(scrapy.Spider):
    name = 'mobile_phone_location'
    allowed_domains = ['www.ip138.com']
    start_urls = ['http://www.ip138.com/']

    def __init__(self, mobile_phone=None, *args, **kwargs):
        super(MobilePhoneLocationSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.ip138.com:8080/search.asp?mobile=%s&action=mobile' % mobile_phone]
        #self.start_urls = ['https://www.baidu.com']

    def parse(self, response):
        item = SpiderMenItem()
        mobile_phone_number = response.xpath("/html/body/table[2]/tr[2]/td[2]/text()").extract()[0]
        item["num_prefix"] = mobile_phone_number[0:7]
        item["area_code"] = response.xpath("/html/body/table[2]/tr[5]/td[2]/text()").extract()[0]
        item["post_code"] = response.xpath("/html/body/table[2]/tr[6]/td[2]/text()").extract()[0].strip()
        card_type_name = response.xpath("/html/body/table[2]/tr[4]/td[2]/text()").extract()[0]
        if u"移动" in card_type_name:
            item["card_type_name"] = u"移动"
            item["card_type"] = "CMCC"
        elif u"联通" in card_type_name:
            item["card_type_name"] = u"联通"
            item["card_type"] = "CUCC"
        else:
            item["card_type_name"] = u"电信"
            item["card_type"] = "CTCC"
        location = response.xpath("/html/body/table[2]/tr[3]/td[2]/text()").extract()[0]
        location = location.replace(u"\xa0", u" ")
        province_city = location.split(u" ")
        item["province"] = province_city[0]
        item["city"] = province_city[1]

        yield item
