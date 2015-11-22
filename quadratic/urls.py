from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from quadratic import views

urlpatterns = patterns('',
   	url(r'^results/', views.quadratic_results, name='quadratic_results'),
   	url(r'^admin/', include(admin.site.urls)),
)
