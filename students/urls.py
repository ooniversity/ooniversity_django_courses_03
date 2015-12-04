from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
                       url(r'^$', views.list_view, name='list_view'),
                       url(r'^([0-9]+)/$', views.detail, name='detail'),
                       url(r'^add/$', views.create, name='add'),
                       url(r'^edit/([0-9]+)/$', views.edit, name='edit'),
                       url(r'^remove/([0-9]+)/$', views.remove, name='remove'),

                       )

