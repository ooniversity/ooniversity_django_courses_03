from django.conf.urls import patterns, include, url
from django.contrib import admin
from coaches.views import detail

urlpatterns = patterns('',
	url(r'^(?P<master_id>\d)/$', detail, name="detail")
	
)