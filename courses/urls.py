from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<course_id>\d+)$', views.detail , name='detail'),
)



