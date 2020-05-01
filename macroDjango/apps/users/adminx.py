# -*- coding:utf-8 -*-
# @Auhor : macro
# @Time  : 2012-01-19
# @Email : macroldj@163.com

import xadmin
from xadmin import views
from .models import *


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "后台管理"
    site_footer = "macroldj@163.com&&macro"
    menu_style = "accordion"


class BannerAdmin:
    """
    轮播图后台
    """
    list_display = ['title', 'add_time']
    list_filter = ['title', 'add_time']
    search_fields = ['title', 'add_time']
    fields = ['title', 'image', 'url', 'add_time']
    model_icon = 'fa fa-photo'


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)