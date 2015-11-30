from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^(?P<coach_id>\d+)/$', detail, name='detail'),
)
