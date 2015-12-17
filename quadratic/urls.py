<<<<<<< HEAD
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^results/$', views.quadratic_results, name='results'),
)
=======
from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

url(r'^quadratic/results/a\=(?P\W{0,30}\w{0,30})\&b\=(?P\W{0,30}\w{0,30})\&c\=(?P\W{0,30}\w{0,30})/$', views.quadratic_results, name='quadratic_results'),


>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
