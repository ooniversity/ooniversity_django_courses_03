from django.conf.urls import patterns, include, url
from django.contrib import admin

from coaches import views

urlpatterns = patterns('',
      # url(r'^$', pybursa.views.index, name="index")  
      url(r'^(?P<coach_id>\d+)/$', views.detail, name = "detail"),
)