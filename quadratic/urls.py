from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic import views
from views import quadratic_results

urlpatterns = patterns('',   
    #url(r'^results/(?P<a>\d+)/(P<b>\d+)/(P<c>\d+)/$', views.quadratic_results, name = 'quadratic_results'),
    url(r'^results/', views.quadratic_results, name = 'quadratic_results'),
)
