from django.conf.urls import url
from users import views


urlpatterns = [
    url(r'^register/', views.register, name='register'), # 注册路由
    url(r'^register_handle/', views.register_handle, name='register_handle'), # 注册处理路由
    url(r'^login/', views.login, name='login'), # 登录路由
    url(r'^login_handle/', views.login_handle, name='login_handle'), # 登陆处理路由
]