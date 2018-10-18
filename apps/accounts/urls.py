# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software:

@site:

@file: urls.py

@time: 2018/10/16 16:15

@desc:

"""
from django.conf.urls import url
from django.contrib.auth.views import (login, logout, password_change,
                                       password_change_done, password_reset,
                                       password_reset_complete,
                                       password_reset_confirm,
                                       password_reset_done)

from . import views

__author__ = 'wanghuagang'

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^password_change/$', password_change, name='password_change'),
    url(r'^password_change/done/$', password_change_done, name='password_change_done'),

    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'), url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/follow/$', views.user_follow, name='user_follow'),
    url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),

    url(r'^$', views.dashboard, name='dashboard'),

]
