# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from tjjttk.items import Record


class TjjttkspiderSpider(scrapy.Spider):
    name = "tjjttkSpider"
    allowed_domains = ["tjjttk.gov.cn"]
    start_urls = ['http://apply.tjjttk.gov.cn/apply/norm/personQuery.html']
    pageNo = 65535
    currentPage = 1

    def start_requests(self):
        yield scrapy.FormRequest(
                self.start_urls[0],
                method='POST',
                formdata={'pageNo': "%d" % (self.currentPage), 'issueNumber': '201707', 'applyCode': ''},
                cookies={'JSESSIONID': '8EE23861EEAE32E876BC6287169C2575-n2.Tomcat1'},
                callback=self.parse,
                dont_filter=True)

    def parse(self, response):
        if self.pageNo == 65535:
            self.pageNo = int(response.css('.f_orange::text').extract()[0])

        for record in response.css('table.ge2_content tr'):
            r = Record()
            r['number'] = record.css('td:nth-child(1)::text').extract_first()
            r['name'] = record.css('td:nth-child(2)::text').extract_first()
            r['year'] = '2017'
            r['month'] = '7'
            yield r

        if self.currentPage <= self.pageNo:
            yield scrapy.FormRequest(
                    self.start_urls[0],
                    method='POST',
                    formdata={'pageNo': "%d" % (self.currentPage), 'issueNumber': '201707', 'applyCode': ''},
                    cookies={'JSESSIONID': '8EE23861EEAE32E876BC6287169C2575-n2.Tomcat1'},
                    callback=self.parse,
                    dont_filter=True)
            self.currentPage += 1
