# coding: utf-8

import re
from users.models import UserSheet
from django.http import JsonResponse
from utils.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


# Create your views here.
# 注册页面
@csrf_exempt
def register(request):
    return render(request, 'users/register.html')


# 注册处理页面
@csrf_exempt
def register_handle(request):
    # 1.获取数据
    username = request.POST.get('name')
    password = request.POST.get('password')
    cwpd = request.POST.get('cwpd')
    email = request.POST.get('email')

    # 验证用户名在数据库中是否存在！！
    is_exist = UserSheet.objects.filter(username=username)
    # 如果存在则提示用户已存在
    if is_exist:
        return JsonResponse({'code': 1})

    # 验证两次密码是否一样
    if password != cwpd:
        return JsonResponse({'code': 2})

    # 进行数据校验
    if not all([username, password, email]):
        # 有数据为空
        return JsonResponse({'code': 3})

    # 邮箱验证
    if not re.match(r'^[a-z0-9][\w\\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', str(email)):
        # 邮箱不合法
        return JsonResponse({'code': 4})

    # 进行业务处理：注册，向用户系统中添加账户
    passport = UserSheet.objects.add_one_user(username=username,
                                              password=password,
                                              email=email)
    passport.objects.save()

    # 注册完毕！
    next_url = request.session.get('url_path', reverse('users:login'))
    return JsonResponse({'code': 5, 'next_url': next_url})


# 登录页面
def login(request):
    return render(request, 'users/login.html')


# 登录处理页面
def login_handle(request):
    pass