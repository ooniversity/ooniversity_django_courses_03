from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^add/$', add, name="add"),
    url(r'^edit/(?P<course_id>\d+)/$', edit, name="edit"),
    url(r'^remove/(?P<course_id>\d+)/$', remove, name="remove"),
    url(r'^(?P<course_id>\d+)/$', detail, name='detail'),
    url(r'^add_lesson/$', add_lesson, name='add-lesson'),
)
