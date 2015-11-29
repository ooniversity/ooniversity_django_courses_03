from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses.views import detail

urlpatterns = patterns('',
    url(r'^(?P<sid>\d)/$', detail, name="detail")
  
)