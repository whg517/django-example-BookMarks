# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software:

@site:

@file: urls.py

@time: 2018/10/17 16:50

@desc:

"""
from django.conf.urls import url

from . import views

__author__ = 'wanghuagang'

urlpatterns = [
    url(r'^create/$', views.image_create, name='create'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.image_detail, name='detail'),
    url(r'^like/$', views.image_like, name='like'),
    url(r'^$', views.image_list, name='list'),
]
