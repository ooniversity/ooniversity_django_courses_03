from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^add/', create, name="add"),
    url(r'^edit/(?P<student_id>\d+)/$', edit, name="edit"),
    url(r'^remove/(?P<student_id>\d+)/$', remove, name="remove"),
    url(r'^(?P<student_id>\d+)/$', detail, name='detail'),
    url(r'^', list_view, name='list_view'),
)
