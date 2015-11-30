from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^(?P<student_id>\d+)/$', detail, name='detail'),
    url(r'^', list_view, name='list_view'),
)
