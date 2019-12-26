# -*- coding: utf-8 -*-

__author__ = 'Jerry Lee'

import scrapy
from ..items import CAPubItem
from scrapy.http import Request
import re


class CAPubSpider(scrapy.Spider):
    name = 'ca_pub'
    allowed_domains = ['www.capub.cn']
    start_urls = ['https://www.capub.cn/']
    download_delay = 5

    def __init__(self, cip_no=None, *args, **kwargs):
        super(CAPubSpider, self).__init__(*args, **kwargs)

        self.global_cip_no = 2019000034
        if cip_no is not None:
            self.global_cip_no = cip_no

        self.start_urls = ['https://www.capub.cn:8443/pdm/business/CipInfoAction.do?method=checkApproveNo&approveNo=%s&captchaNo=&chk=on' % self.global_cip_no]

    def parse(self, response):
        #print response.text

        if response.text.find(u'核字号错误或位数不正确') == 0:
            item = CAPubItem()

            item["cip_no"] = response.xpath('//div[@id="info"]/table/tr[2]/td[2]/text()').extract()[0]
            item["book_name"] = response.xpath('//div[@id="info"]/table/tr[3]/td[2]/text()').extract()[0]
            item["publisher"] = response.xpath('//div[@id="info"]/table/tr[5]/td[2]/text()').extract()[0]
            item["publish_datetime"] = response.xpath('//div[@id="info"]/table/tr[6]/td[4]/text()').extract()[0]
            owner = response.xpath('//*[@id="info"]/table/comment()[1]').extract()[0]
            if owner is not None:
                try:
                    texts = re.findall(r'<td.*?>(.*?)</td>', owner, re.S|re.M)
                    item["owner"] = texts[1].split('<')[0]
                except Exception, e:
                    print(str(e))
            content = response.xpath('//*[@id="print"]/table/tr[3]/td/pre/p/text()').extract()[0]

            if content is not None and len(content) > 0:
                try:
                    item["author"] = content.split('/')[1].split('.')[0].strip()
                except Exception, e:
                    print str(e)

            print(item)

            yield item

        self.global_cip_no += 1
        if self.global_cip_no <= 2019020480:
            url = 'https://www.capub.cn:8443/pdm/business/CipInfoAction.do?method=checkApproveNo&approveNo=%s&captchaNo=&chk=on' % self.global_cip_no
            print url
            yield Request(url, callback=self.parse)



