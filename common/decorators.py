# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software:

@site:

@file: decorators.py

@time: 2018/10/18 11:48

@desc:

"""

__author__ = 'wanghuagang'

from django.http import HttpResponseBadRequest


def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
