from django.conf.urls import patterns, url, include
from django.contrib import admin

from students import views

urlpatterns = patterns('',
	url(r'^$', views.list_view, name = "list_view"),
	url(r'^(?P<student_id>\d+)/$', views.detail, name = "detail"),
	)