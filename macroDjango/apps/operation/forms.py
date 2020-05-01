# -*- coding:utf-8 -*-
# @Auhor : macro
# @Time  : 2012-01-19
# @Email : macroldj@163.com

from django import forms

from .models import *


class CommentsForm(forms.Form):
    comment = forms.CharField(required=True)

