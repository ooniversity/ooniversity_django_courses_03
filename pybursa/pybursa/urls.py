from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from pybursa import views
#from quadratic import views
from quadratic.views import quadratic_results, quadratic_start


urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),

    url(r'^quadratic/results/$', quadratic_results, name='quadratic_results'),
    
    url(r'^admin/', include(admin.site.urls)),
)