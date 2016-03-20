# -*- coding: utf8 -*-
import requests
import sys

class Filter(object):

    """Docstring for Filter. """

    def __init__(self):
        super(Filter, self).__init__

    def filter(self, keyword, url):
        """@todo: Docstring for filter.

        :keyword: 包含的关键字
        :url: 被测试的地址
        :returns: 包含关键字返回地址，否则返回None

        """
        try:
            response = requests.get(url, timeout = 1)
            content = response.content
            if content and (content.find(keyword) > 0):
                return url
            else:
                return None
        except:
            return None

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print '[    Filter-URL-Tool                       ]'
        print '[   edit by richard_ma                     ]'
        print '[ any issues:richard.ma.19850509@gmail.com ]'
        keyword = raw_input('keyword for filtering: >')
        url = raw_input('url want to be filterd? >')
    elif len(sys.argv) == 3:
        # 添加命令行参数，方便shell调用
        # python bing.py keyword url
        keyword, url = sys.argv[1:3]
    else:
        print 'Usage: python bing.py [keyword] [url]'
        sys.exit(1)

    f = Filter()
    if f.filter(keyword, url) != None:
        print url
