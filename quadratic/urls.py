from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

url(r'^quadratic/results/a\=(?P\W{0,30}\w{0,30})\&b\=(?P\W{0,30}\w{0,30})\&c\=(?P\W{0,30}\w{0,30})/$', views.quadratic_results, name='quadratic_results'),


