from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>[1-3]{1})/$', views.detail, name = "detail")
)