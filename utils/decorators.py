# coding: utf-8

from django.shortcuts import redirect
from django.core.urlresolvers import reverse


# 登录判断
def login_required(views_func):
    '''登录判断装饰器'''
    def wrapper(request, *views_args, **views_kwargs):
        if request.session.has_key('is_login'):
            # 用户已登录
            return views_func(request, *views_args, **views_kwargs)

        else:
            # 跳转到登录页
            return redirect(reverse('users:login'))

    return wrapper