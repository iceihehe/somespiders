# -*- coding=utf-8 -*-
# Created Time: 2015年07月07日 星期二 15时49分40秒
# File Name: datatang.py

from __future__ import print_function

import scrapy
from pyquery import PyQuery

from tools import html_clean
from ..items import TestItem

base_url = 'http://www.datatang.com'


class DatatangSpider(scrapy.Spider):
    '''
    数据堂爬虫
    '''
    name = 'datatang'
    start_urls = [
        'http://www.datatang.com/data/list/r020-t01-la01-p1',
        'http://www.datatang.com/data/list/r020-t02-la01-p1',
        'http://www.datatang.com/data/list/r020-t03-la01-p1',
        'http://www.datatang.com/data/list/r020-t04-la01-p1',
        'http://www.datatang.com/data/list/r020-t04-la02-p1',
        'http://www.datatang.com/data/list/r020-t03-la02-p1',
        'http://www.datatang.com/data/list/r020-t02-la02-p1',
        'http://www.datatang.com/data/list/r020-t01-la02-p1',
    ]
    """
    start_urls = [
        'http://www.datatang.com/data/list/r020-t01-la01-p1',
    ]
    """

    def parse(self, response):
        pq = PyQuery(response.body)
        try:
            max_url = pq("div.page_url")("a[title=%s]" % (u'末页')) \
                .attr('href').split('p')[-1]
        except:
            max_url = '1'
        if 'la01' in response.url:
            lang = u'中文'
        else:
            lang = u'英文'
        if 't01' in response.url:
            data_type = 'text'
        elif 't02' in response.url:
            data_type = 'voice'
        elif 't03' in response.url:
            data_type = 'video'
        else:
            data_type = 'image'
        self.data_type = data_type
        self.lang = lang
        for i in xrange(int(max_url)):
            yield scrapy.Request(
                response.url[:-1]+str(i),
                callback=self.secondparse
            )

    def secondparse(self, response):
        pq = PyQuery(response.body)
        for i in pq('div.con_box')('h5')('a'):
            yield scrapy.Request(
                base_url+i.attrib['href'],
                callback=self.thirdparse
            )

    def thirdparse(self, response):
        a, b, c, d, e, f, g, h = html_clean(response.body_as_unicode())
        if not a:
            print('************************************************')
            return
        item = TestItem()
        item['title'] = a
        item['capacity'] = b
        item['details'] = c
        item['published_time'] = d
        item['download'] = e
        item['price'] = f
        item['preview'] = g
        item['data_category'] = h

        item['lang'] = self.lang
        item['data_type'] = self.data_type
        item['source'] = u'数据堂'
        item['url'] = response.url
        yield item
