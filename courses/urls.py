from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^add/$', create, name="add"),
    url(r'^edit/(?P<course_id>\d+)/$', edit, name="edit"),
    url(r'^remove/(?P<course_id>\d+)/$', remove, name="remove"),
    url(r'^(?P<course_id>\d+)/$', detail, name='detail'),
    url(r'^add_lesson/(?P<course_id>\d+)/$', add_lesson, name='add-lesson'),
)
