from django.conf.urls import patterns, url, include
from django.contrib import admin

from courses import views


urlpatterns = patterns('',
	url(r'^(?P<course_id>\d+)/$', views.detail, name = "detail"),
	)
