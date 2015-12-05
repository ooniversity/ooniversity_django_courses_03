from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
	url(r'^$', views.list_view, name='list_view'),
	url(r'^(?P<detail_id>\d+)/$', views.detail, name='detail'),
	url(r'^apply/$', views.apply_to_course, name='apply'),
    url(r'^edit_application/(?P<pk>\d+)/$', views.edit_application, name='edit_application'),
	url(r'^delete_application/(?P<pk>\d+)/$', views.delete_application, name='delete_application'),
	url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
)
