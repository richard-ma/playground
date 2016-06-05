#!/usr/bin/env python

import requests
import re
import datetime
import time

def getHeaders():
    return {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
    }

def strDate(date):
    return date.strftime("%Y-%m-%d")

today = datetime.datetime.now()
end_time = datetime.datetime(2015, 1, 1)

start = today - datetime.timedelta(days=1)
end = end_time

loop_times = (start - end).days
current_day = start
for d in xrange(0, loop_times + 1):
    date = strDate(current_day)
    #print date

    url = "http://news.baidu.com/%s/view.html" % (date)
    #print url
    response = requests.get(url, headers=getHeaders()).content
    #print response

    reg_expression = r'<a href=".*?" target="_blank" class="a3" .*?>.*?</a>'
    messages = re.findall(reg_expression, response)
    #print messages

    for message in messages:
        title = re.findall(r'>(.*)</a>', message)[0].decode('gbk').encode('utf-8')
        link = re.findall(r'href="(.*?)"', message)[0]
        print date + ',',
        print title + ',',
        print link

    current_day = current_day - datetime.timedelta(days=1)
