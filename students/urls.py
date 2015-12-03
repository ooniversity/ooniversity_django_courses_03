from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views


urlpatterns = patterns('',
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.list_view, name='list_view'),
)



