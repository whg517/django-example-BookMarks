# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software:

@site:

@file: authentication.py

@time: 2018/10/17 13:48

@desc:

"""
from django.contrib.auth.models import User

__author__ = 'wanghuagang'


class EmailAuthBackend(object):
    """
    Authenticate using e-mail account.
    """

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
