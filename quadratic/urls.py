# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import quadratic_results

urlpatterns = patterns('',
                       url(r'results/$', quadratic_results, name='results'),
                       )
