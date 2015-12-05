from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.list_view, name='list_view'),
	url(r'add/$', views.create , name = "add" ),
	url(r'^edit/(?P<s_id>[0-9]+)/$', views.edit, name = "edit"),
	url(r'^remove/(?P<s_id>[0-9]+)/$', views.remove, name = "remove"),
    )
