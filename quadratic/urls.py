# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from quadratic import views

from .views import quadratic_results


urlpatterns = patterns('',
	url(r'results/$', quadratic_results, name='result'),
 )