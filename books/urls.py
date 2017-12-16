from django.conf.urls import url
from books import views


urlpatterns = [
    url(r'^index/', views.index, name='index'), # 主页路由
]