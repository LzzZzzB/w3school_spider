# !/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector
from w3school.items import W3schoolItem


class W3schoolSpider(Spider):
    name = "w3school"
    allowed_domains = ["w3school.com.cn"]
    start_urls = [
        "http://www.w3school.com.cn/xml/xml_syntax.asp"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@id="navsecond"]/div[@id="course"]/ul[1]/li')

        items = []
        for site in sites:
            item = W3schoolItem()
            title = site.xpath('a/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('a/@title').extract()

            item['title'] = title
            item['link'] = link
            item['desc'] = desc
            items.append(item)

        return items