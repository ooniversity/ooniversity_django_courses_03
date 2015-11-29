from django.conf.urls import patterns, include, url
from django.contrib import admin
from students.views import list_view, detail

urlpatterns = patterns('',
	
	url(r'^(?P<student_id>\d)/$', detail, name="detail"),
	url(r'^', list_view, name="list_view"),
	
	
)