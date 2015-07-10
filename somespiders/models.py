# -*- coding=utf-8 -*-

from mongoengine import Document, StringField, DateTimeField,\
    FloatField, IntField, ListField


class Shujutao(Document):
    '''数据淘数据文档'''
    # 数据标题
    title = StringField()
    # 数据大小
    capacity = FloatField()
    # 发布时间
    published_time = DateTimeField()
    # 描述信息
    details = StringField()
    # 下载量
    download = StringField()
    # 点击量
    click = StringField()
    # 原始链接
    url = StringField()
    # 数据源
    source = StringField()
    # 数据类型
    data_type = StringField()
    # 我们平台的点击量
    hits = IntField(default=0)
    # 数据标价类型
    price = StringField()
    # 数据预览(链接)
    preview = ListField(StringField())
    # 联系人
    contact = StringField()
    # 语言
    lang = StringField()
    # 数据分类
    data_category = StringField()


class Feedback(Document):
    '''建议反馈'''
    title = StringField()
    description = StringField()
    pic = StringField()
    contact = StringField()
