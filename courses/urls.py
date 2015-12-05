from django.conf.urls import patterns, url, include
from django.contrib import admin

from courses import views


urlpatterns = patterns('',
	url(r'^(?P<course_id>\d+)/$', views.detail, name = "detail"),
    url(r'^add/', views.add, name="add"),
    url(r'^edit/(?P<course_id>\d+)/$', views.edit, name="edit"),
    url(r'^remove/(?P<course_id>\d+)/$', views.remove, name="remove"),	
	)
