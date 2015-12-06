from django.conf.urls import patterns, url
from students import views


urlpatterns = patterns('',
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<request_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^edit/(?P<request_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<request_id>\d+)/$', views.remove, name='remove'),
)