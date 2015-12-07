from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
        url(r'^$', views.list_view, name='list_view'),
        url(r'^(\d{1})/$', views.detail, name='detail'),
        url(r'add/$', views.create, name='add'),
        url(r'^edit/(?P<stdnt_id>\d+)/$', views.edit, name='edit'),
        url(r'remove/(?P<stdnt_id>\d+)/$', views.remove, name='remove'),
        )
