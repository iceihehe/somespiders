# -*- coding=utf-8 -*-
# Created Time: 2015年06月16日 星期二 17时29分56秒
# File Name: tools.py

from __future__ import print_function
import datetime

from pyquery import PyQuery


def capacity_clean(data):
    '''处理数据大小'''
    try:
        num = float(data[:-1])
    except:
        # 数据大小默认0
        return 0
    units = data[-1].lower()
    if units == 'g':
        num *= float(1000)
    elif units == 'k':
        num /= float(1000)
    return num


def html_clean(html):
    '''处理request.text'''
    d = PyQuery(html)

    # 判断是否已经下架
    if u'此数据已下架' in html:
        return False, False, False, False, False, False, False, False

    # 下载量默认0
    download = '0'

    metadata = d('div.metadata').text()
    # 有简介
    if metadata:
        details = d('#details_1').text()
    # 没有简介，只有flash
    else:
        ss = d('#details_1').text()
        details = ss[ss.find('</a>");') + 8:]

    # 数据标题
    title = d('h1.fs14').text()

    # 时间和下载量
    for i in d('.fc_gray3.mb10'):
        if u'时间' in i.text:
            published_time = datetime.datetime.strptime(
                i.text[4:], '%Y-%m-%d %H:%M'
            )
        if u'下载' in i.text:
            download = i.text.split()[1]
    # 数据大小
    ss = d('h2.fs14.fc_gray6').text()[5:]
    capacity = capacity_clean(ss)
    # 数据标价
    price = d('h2.fc_red').text()[5:].split()
    if not price:
        price = 'free'
    elif u'积分' in price:
        price = 'score'
    else:
        price = 'pay'
    # 数据预览(链接)
    imgs = []
    ss = d('#details_1')('img')
    for i in ss:
        if 'jpg' in i.attrib['src']:
            imgs.append(i.attrib['src'])

    # 数据分类
    category = d('div.path_box')('a')[-1].text

    return title, capacity, details, published_time, download, price, imgs, category
