# -*- coding:utf-8 -*-
# @Auhor : macro
# @Time  : 2012-01-25
# @Email : macroldj@163.com

import xadmin
from xadmin import views

from .models import *


class NewsAdmin:
    """
    新闻后台管理
    """
    list_display = ['title', 'checknum', 'classification', 'add_times']
    list_filter = ['checknum', 'classification', 'add_times']
    search_fields = ['title', 'checknum', 'classification', 'add_times']
    fields = ['title', 'content', 'image', 'checknum', 'classification', 'add_times']
    readonly_fields = ['checknum']
    model_icon = 'fa fa-newspaper-o'
    style_fields = {"content": "ueditor"}


xadmin.site.register(News, NewsAdmin)
