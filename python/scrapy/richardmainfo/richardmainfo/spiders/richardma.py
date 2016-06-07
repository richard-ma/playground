# -*- coding: utf-8 -*-
import scrapy


class RichardmaSpider(scrapy.Spider):
    name = "richardma"
    allowed_domains = ["richardma.info"]
    start_urls = (
        'http://www.richardma.info/',
    )

    def parse(self, response):
        idx = 0
        for sel in response.xpath('//ul/li'):
            if idx == 0:
                idx = 1
                continue
            print sel.xpath('//a/text()').extract()
