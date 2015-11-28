from django.conf.urls import patterns, url
from students.views import list_view
from students.views import detail

urlpatterns = patterns('',
    url(r'^$', list_view, name='list_view'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
    )