from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^students/(?P<student_id>\d+)/$', detail, name='detail'),
    url(r'^students/', list_view, name='list_view'),
)
