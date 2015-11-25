from django.conf.urls import patterns, include, url
from django.contrib import admin
from students.views import list_view

urlpatterns = patterns('',
	url(r'^', list_view, name="list_view"),
	
)
