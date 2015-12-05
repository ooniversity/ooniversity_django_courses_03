from django.conf.urls import patterns, url
from students.views import list_view, detail, create, edit, remove


urlpatterns = patterns('',
    url(r'^$', list_view, name='list_view'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^add/$', create, name='create'),
    url(r'^edit/(?P<pk>\d+)/$', edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', remove, name='remove'),
    )