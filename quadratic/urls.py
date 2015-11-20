# -*- coding: utf-8 -*-
__author__ = 'dimon'
from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^results/$'),

)