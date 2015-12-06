from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<course_id>\d+)$', views.detail, name='detail'),
    url(r'^(?P<course_id>\d+)/add-lesson/$', views.add_lesson, name='add-lesson'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<course_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<course_id>\d+)/$', views.remove, name='remove'),
    )




