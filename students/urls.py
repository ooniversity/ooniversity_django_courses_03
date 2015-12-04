from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.list_view, name='list'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
	url(r'^add/$', views.create, name='add'),
    url(r'^edit/$', views.edit, name='edit'),
	url(r'^remove/$', views.remove, name = "remove")
)